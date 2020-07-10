from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.py')


# print(f"BASE_DIR: {app.config['BASE_DIR']}")
# app.config['BASE_DIR']


# from models import *
from routes import *