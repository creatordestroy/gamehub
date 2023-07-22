from peewee import *
from app.database import db
from app.models.product import Product
from app.models.storeLocation import StoreLocation

class LowInventory(db.Model):

    lowinv_id = PrimaryKeyField()
    product_id = ForeignKeyField(Product, backref="LowInventory")
    store_id = ForeignKeyField(StoreLocation, backref='LowInventory')
    threshold = IntegerField()

    class Meta:
        database = db
        table_name = 'LowInventory'