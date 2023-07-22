from peewee import *
from app.database import db
from app.models.storeLocation import StoreLocation
from app.models.product import Product

class Inventory(db.Model):

    inventory_id = PrimaryKeyField()
    store_id = ForeignKeyField(StoreLocation, backref='Inventory')
    product_id = ForeignKeyField(Product, backref='Inventory')
    product_stock = IntegerField()
    
    class Meta:
        database = db
        table_name = 'Inventory'
