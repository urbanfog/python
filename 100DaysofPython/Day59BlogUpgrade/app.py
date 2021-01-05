from flask import Flask, render_template, request
import requests
import smtplib
import os

# Load ENV variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.GETENV("MY_PASS")


class Post:
    def __init__(self, post_id, title, body, date, author, subtitle, image_url) -> None:
        self.id = post_id
        self.title = title
        self.body = body
        self.date = date
        self.author = author
        self.subtitle = subtitle
        self.image_url = image_url


app = Flask(__name__)
all_data = requests.get(
    "https://api.npoint.io/43644ec4f0013682fc0d").json()
all_blog_posts = []
for p in all_data:
    post = Post(post_id=p['id'],
                title=p['title'],
                body=p['body'],
                date=p['date'],
                author=p['author'],
                subtitle=p['subtitle'],
                image_url=p['image_url'])
    all_blog_posts.append(post)


def send_email(message, send_to):
    msg = f"Subject: New Request!\n\n{message}".encode(encoding="utf8")
    with smtplib.SMTP("smtp.live.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=send_to,
                            msg=msg)


@app.route('/')
def home_page():
    return render_template("index.html", all_blog_posts=all_blog_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    h1 = None
    if request.method == 'GET':
        h1 = 'Contact Me'
    if request.method == 'POST':
        contact_form_data()
        h1 = 'Successfully submitted form'
        message = f'''
            Name: {request.form["name"]}
            Email: {request.form["email"]}
            Phone: {request.form["phone_number"]}
            Message: {request.form["message"]}
            '''
        send_email(send_to="jamescsmith@live.com", message=message)
    return render_template("contact.html", h1=h1)


def contact_form_data():
    print(request.form['name'])


@app.route('/post/<int:id>')
def post_page(id):
    requested_post = None
    for post in all_blog_posts:
        if post.id == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
