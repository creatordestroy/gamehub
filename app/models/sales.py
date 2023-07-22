from peewee import *
from app.database import db
from app.models.inventory import Inventory
from app.models.storeLocation import StoreLocation

class Sales(db.Model):

    sale_id = PrimaryKeyField()
    product_id = ForeignKeyField(Inventory, backref="Sales")
    store_id = ForeignKeyField(StoreLocation, backref="Sales")
    sale_date = DateField()
    sale_quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'Sales'