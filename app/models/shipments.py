from peewee import *
from app.database import db
from app.models.inventory import Inventory

class Shipments(db.Model):

    shipment_id = PrimaryKeyField()
    product_id = ForeignKeyField(Inventory, backref="Shipments")
    shipment_id = DateField()
    shipment_quantity = IntegerField()

class Meta:
    database = db