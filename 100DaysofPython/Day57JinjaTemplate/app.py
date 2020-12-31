from flask import Flask
from flask import render_template
import datetime
from person import Person
import requests
from post import Post

app = Flask(__name__)
all_posts = all_posts = requests.get(
    "https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []

for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home_page():
    year = datetime.datetime.today().year
    return render_template("index.html",
                           current_year=year)


@app.route('/guess/<name>')
def guesser(name):
    person = Person(name=name)
    return render_template("guess.html",
                           name=person.name,
                           gender=person.gender,
                           age=person.age,
                           country=person.country,
                           )


@app.route('/blog')
def blog():
    return render_template("blog.html", posts=post_objects)


@app.route('/post/<int:id>')
def blog_post(id):
    requested_post = None
    for post in post_objects:
        if post.id == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
