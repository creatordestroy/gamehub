from peewee import *
from app.database import db
from app.models.inventory import Inventory

class LowOrders(db.Model):

    lowinv_id = PrimaryKeyField()
    product_id = ForeignKeyField(Inventory, backref="LowOrders")
    threshold = IntegerField()
    date_reported = DateField()

class Meta:
    database = db