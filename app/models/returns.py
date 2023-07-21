from peewee import *
from app.database import db
from app.models.inventory import Inventory
from app.models.user import User

class Returns(db.Model):

    return_id = PrimaryKeyField()
    product_id = ForeignKeyField(Inventory, backref="Returns")
    user_id = ForeignKeyField(User, backref="Returns")
    return_date = DateField()
    return_reason = CharField()

class Meta:
    database = db