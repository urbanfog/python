from flask import Flask
from flask import render_template
import requests


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


@app.route('/')
def home_page():
    return render_template("index.html", all_blog_posts=all_blog_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<int:id>')
def post_page(id):
    requested_post = None
    for post in all_blog_posts:
        if post.id == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
