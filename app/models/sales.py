from peewee import *
from app.database import db
from app.models.product import Product
from app.models.storeLocation import StoreLocation

class Sales(db.Model):

    sale_id = PrimaryKeyField()
    product_id = ForeignKeyField(Product, backref="Sales")
    store_id = ForeignKeyField(StoreLocation, backref="Sales")
    sale_date = DateField()
    quantity_sold = IntegerField()

    class Meta:
        database = db
        table_name = 'Sales'