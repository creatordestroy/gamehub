from peewee import *
from app.database import db

class Inventory(db.Model):

    #__tablename__ = 'Inventory'
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255)
    product_cost = DecimalField(decimal_places=2)
    product_stock = IntegerField()
    product_rating = DecimalField(decimal_places=2)
    product_review = CharField(max_length=255)
    

    class Meta:
        database = db
        table_name = 'Inventory'
