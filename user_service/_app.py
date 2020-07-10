import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Config
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB init
db = SQLAlchemy(app)

# Marshmallow init
ma = Marshmallow(app)


# Models
class Something(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    qty  = db.Column(db.Integer)

    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

# Schema
class SomethingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'qty')

# Init Schema
something_schema  = SomethingSchema()
somethings_schema = SomethingSchema(many=True)

# Create DB
db.create_all()

# Get all
@app.route('/', methods=['GET'])
def index():
    all_something = Something.query.all()
    result = somethings_schema.dump(all_something)
    return jsonify(result)

# Get by id
@app.route('/something/get/<id>', methods=['GET'])
def get_someting(id):
    something = Something.query.get(id)
    return something_schema.jsonify(something)

# Create new
@app.route('/something/add', methods=['POST'])
def add_someting():
    name = request.json['name']
    qty  = request.json['qty']

    new_something = Something(name, qty)

    db.session.add(new_something)
    db.session.commit()

    return something_schema.jsonify(new_something)

# Update existing
@app.route('/something/update/<id>', methods=['PUT'])
def update_someting(id):
    something = Something.query.get(id)

    name = request.json['name']
    qty  = request.json['qty']

    something.name = name
    something.qty  = qty

    db.session.commit()

    return something_schema.jsonify(something)

# Delete by id
@app.route('/something/delete/<id>', methods=['DELETE'])
def delete_someting(id):
    something = Something.query.get(id)
    db.session.delete(something)
    db.session.commit()
    return something_schema.jsonify(something)