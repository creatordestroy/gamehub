from peewee import *
from app.database import db
from .user import User

class Inventory(Model):
    title = CharField()
    platform = CharField()
    quantity = IntegerField()
    warning_quantity = IntegerField()
    user = ForeignKeyField(User, backref='inventories')

    class Meta:
        database = db
