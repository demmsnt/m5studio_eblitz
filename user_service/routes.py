from app import app
from flask import request, jsonify

from models import *


@app.route('/')
def index():
    return 'Hello, World! =))'


@app.route('/createdb')
def create_db():
    db.create_all()
    return 'DB created'

"""
# Get all
@app.route('/something', methods=['GET'])
def someting_list():
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
"""