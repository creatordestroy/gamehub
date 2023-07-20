from peewee import *
from app.database import db
from app.models.inventory import Inventory

class OrderForm(db.Model):

    #__tablename__ = 'ProductOrders'
    order_id = PrimaryKeyField()
    product_id = ForeignKeyField(Inventory, backref='OrderForm')
    order_date = DateField()
    order_quantity = IntegerField()

    class Meta:
        database = db