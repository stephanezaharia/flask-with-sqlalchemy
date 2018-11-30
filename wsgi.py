# wsgi.py
import os
import logging
from flask import Flask,request,jsonify,render_template
from config import Config

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow # Order is important here!




app = Flask(__name__)

app.config.from_object(Config)
ma = Marshmallow(app)

db = SQLAlchemy(app)
from models import Product
from schemas import products_schema,product_schema

@app.route('/')
def main():
    # Use this in the home route
    products = db.session.query(Product).all()
    return render_template('home.html', title="Products",products=products)

@app.route('/details/<int:id>')
def details(id):
    # Use this in the home route
    product = db.session.query(Product).get(id)
    return render_template('details.html', title="Product detail",product=product)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/products',methods=["POST","GET"])
def products():
    if request.method=="GET":
        products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
        return products_schema.jsonify(products)
    if request.method=="POST":
        json=request.json
        prod = Product()
        prod.name = json["name"]
        prod.description = json["description"]
        db.session.add(prod)
        db.session.commit()
        #insert product
        return product_schema.jsonify(prod)

@app.route('/product/<int:id>',methods=["GET","DELETE"])
def product(id):
    if request.method=="GET":
        product=db.session.query(Product).get(id)
        print(product)
        return product_schema.jsonify(product)
    elif request.method=="DELETE":
        try:
            db.session.query(Product).\
                filter(Product.id == id).delete()
            db.session.commit()
            return jsonify({"status":"deleted","id":id})
        except Exeption as e:
            return jsonify({"status":"error","description":str(e)})

