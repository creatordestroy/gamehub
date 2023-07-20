from peewee import *
from app.database import db

class User(db.Model):
    
    #__tablename__ = 'User'
    customer_id = PrimaryKeyField()
    customer_name = CharField(max_length=255)
    customer_email = CharField(max_length=255)
    customer_address = CharField(max_length=255)

    class Meta:
        database = db
