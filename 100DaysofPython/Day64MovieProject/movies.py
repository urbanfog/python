from flask_sqlalchemy import SQLAlchemy


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, unique=True)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        '''Allows the book object to be identified by its title when printed'''
        return f"<Book {self.title}>"


db.create_all()
