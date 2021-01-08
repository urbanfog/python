from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books.collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, unique=True)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        '''Allows the book object to be identified by its title when printed'''
        return f"<Book {self.title}>"


db.create_all()


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = SelectField("Rating", choices=[
                         1, 2, 3, 4, 5], validators=[DataRequired()])
    add = SubmitField("Add")


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.data['title'],
            author=form.data['author'],
            rating=form.data['rating']
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html', form=form)


@app.route("/edit/<id>")
def edit():
    return render_template('edit.html')


if __name__ == "__main__":
    app.run(debug=True)
