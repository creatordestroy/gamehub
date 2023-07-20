from peewee import *
from app.database import db

class Inventory(db.Model):

    __tablename__ = 'Inventory'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.varchar(255), nullable=False)
    product_cost = db.Column(db.Float, nullable=False)
    product_stock = db.Column(db.Integer, nullable=False)
    

    class Meta:
        database = db
