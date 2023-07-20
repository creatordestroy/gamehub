from peewee import *
from app.database import db
import sqlalchemy

class Inventory(db.Model):

    #__tablename__ = 'Inventory'
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255)
    product_cost = DecimalField(decimal_places=2)
    product_stock = IntegerField()
    

    class Meta:
        database = db
