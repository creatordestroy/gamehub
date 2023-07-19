from peewee import *
from app.models.user import User
from app.models.inventory import Inventory
from app.database import db

class WishList(Model):
    user = ForeignKeyField(User, backref='wishlist')
    inventory = ForeignKeyField(Inventory, backref='wishlisted_by')

    class Meta:
        database = db