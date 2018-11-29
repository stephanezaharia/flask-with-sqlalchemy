# wsgi.py
import os
import logging
from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow # Order is important here!


logging.warn(os.environ["DUMMY"])

app = Flask(__name__)

app.config.from_object(Config)
ma = Marshmallow(app)

db = SQLAlchemy(app)
from models import Product
from schemas import products_schema




@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)

