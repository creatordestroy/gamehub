from peewee import *
from app.database import db
from app.models.product import Product
from app.models.storeLocation import StoreLocation

class ProductOrders(db.Model):

    order_id = PrimaryKeyField()
    store_id = ForeignKeyField(StoreLocation, backref='ProductOrders')
    product_id = ForeignKeyField(Product, backref='ProductOrders')
    order_status = CharField(max_length=255)
    order_date = DateField()
    order_quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'ProductOrders'