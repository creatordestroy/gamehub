from peewee import *
from app.database import db

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    role = CharField()

    class Meta:
        database = db
