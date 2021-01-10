from logging import error
from flask import Flask, json, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)
    return jsonify(cafe.to_dict())

# HTTP GET - Read Record


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=all_cafes)


@app.route("/search")
def search_cafes():
    search_term = request.args.get('loc')
    results = Cafe.query.filter_by(location=search_term).all()
    all_cafes = [cafe.to_dict() for cafe in results]
    if len(all_cafes) == 0:
        return jsonify(error={"Not Found": "Sorry we don't have a cafe in that location"}), 404
    return jsonify(cafes=all_cafes)
# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():
    req = request.form
    cafe = Cafe(
        name=req.get('name'),
        map_url=req.get('map_url'),
        img_url=req.get('img_url'),
        location=req.get('location'),
        seats=req.get('seats'),
        has_toilet=bool(req.get('has_toilet')),
        has_wifi=bool(req.get('has_wifi')),
        has_sockets=bool(req.get('has_sockets')),
        can_take_calls=bool(req.get('can_take_calls')),
        coffee_price=req.get('coffee_price'),
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"Success": "Cafe added"}), 200

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<id>", methods=["PATCH"])
def update_coffee_price(id):
    new_price = request.form.get('coffee_price')
    cafe = Cafe.query.filter_by(id=id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Price updated successfully."}), 200
    else:
        return jsonify(response={"Failure": "Could not find resource."}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args.get('api_key')
    if api_key == 'TOPSECRETAPIKEY':
        cafe = Cafe.query.filter_by(id=id).first()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Cafe deleted successfully."}), 200
        else:
            return jsonify(response={"Failure": "Resource could not be found."}), 404
    else:
        return jsonify(response={"Failure": "You do not have access to delete resource."}), 403


if __name__ == '__main__':
    app.run(debug=True)
