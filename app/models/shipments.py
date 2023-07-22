from peewee import *
from app.database import db
from app.models.product import Product
from app.models.storeLocation import StoreLocation

class Shipments(db.Model):

    shipment_id = PrimaryKeyField()
    store_id = ForeignKeyField(StoreLocation, backref="Shipments")
    product_id = ForeignKeyField(Product, backref="Shipments")
    shipment_date = DateField()
    quantity_shipped = IntegerField()

    class Meta:
        database = db
        table_name = 'Shipments'