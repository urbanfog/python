from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.sql.schema import UniqueConstraint
from wtforms import StringField, SubmitField, SelectField
import wtforms
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

# Bootstrap and WTForms
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Create DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Create DB table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False, unique=True)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        '''Allows the book object to be identified by its title when printed'''
        return f"<Movie {self.title}>"


db.drop_all()
db.create_all()


class RateMovieForm(FlaskForm):
    rating = SelectField("Rating", choices=[
                         1, 2, 3, 4, 5], validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    add = SubmitField("Update")


class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    add = SubmitField("Add")


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    if form.validate_on_submit():
        movie = Movie.query.filter_by(id=id).first()
        movie.rating = form.data['rating']
        movie.review = form.data['review']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        requested_movie = Movie.query.get(id)
        return render_template("edit.html", movie=requested_movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


def find_movies(movie_title) -> list:
    movies = []
    end_point = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "apikey",
        "language": "en-US",
        "query": movie_title,
        "include_adult": False,
    }
    response = requests.get(end_point, params=params).json()
    json = response['results']
    print(json[0])
    for movie in json:
        new_movie = {
            "title": movie['original_title'],
            "year": movie['release_date'][0:4],
            "movie_id": movie['id']
        }
        movies.append(new_movie)
        print(movies)
    return movies


def get_movie_details(id) -> Movie:
    end_point = f"https://api.themoviedb.org/3/movie/id"
    params = {
        "api_key": "6840d15394ea54ff091fe135c445ba3c",
        "language": "en-US",
    }
    response = requests.get(end_point, params=params).json()
    print(response)

    # json = response['results']
    # for movie in json:
    #     new_movie = {
    #         "title": movie['original_title'],
    #         "year": movie['release_date'][0:4],
    #     }
    #     movies.append(new_movie)
    #     print(movies)
    # return movies


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        print(form.data['title'])
        movie_list = find_movies(form.data['title'])
        print(movie_list)
        return render_template("select.html", movies=movie_list)
    return render_template("add.html", form=form)


@ app.route("/select")
def select(movies):
    return render_template('select.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
