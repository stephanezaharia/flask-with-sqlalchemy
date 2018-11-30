# models.py
from wsgi import db
from datetime import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.Text())
    dc = db.Column(db.DateTime,default=datetime.now())
    category_id = db.Column(db.Integer, ForeignKey('categories.id'))
    category = relationship("Category")

    def __repr__(self):
        return f'<id {self.id} category {self.category} dc {self.dc}>'


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
