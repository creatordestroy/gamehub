from peewee import *
from app.database import db

class User(db.Model):
    
    #__tablename__ = 'User'
    user_id = PrimaryKeyField()
    user_name = CharField(max_length=255)
    user_email = CharField(max_length=255)
    user_address = CharField(max_length=255)

    class Meta:
        database = db
        table_name = 'User'
