#!/usr/bin/env python3
""" basic flask app
"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from add_data import add_data_to_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'


# Create the tables
with app.app_context():
    db.create_all()
    # Add data to the database
    add_data_to_database(db, Drink)


@app.route('/')
def index():
    return 'My name is Abdallah and I am a software engineer!'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    drinks_list = []
    for drink in drinks:
        drinks_list.append({'name': drink.name, 'description': drink.description})
    return {"drinks": drinks_list}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({"name": drink.name, "description": drink.description})

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return jsonify({"id": drink.id})


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)
    db.session.delete(drink)
    db.session.commit()
    return jsonify({"id": drink.id})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
