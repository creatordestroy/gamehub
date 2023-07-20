from peewee import *
from app.database import db

class User(db.Model):
    
    __tablename__ = 'User'
    customer_id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.varchar(255), nullable = False)
    customer_email = db.Column(db.varchar(255), nullable = False)
    customer_address = db.Column(db.varchar(255), nullable = False)

    class Meta:
        database = db
