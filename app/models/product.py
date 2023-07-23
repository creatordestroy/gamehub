from peewee import *
from app.database import db

class Product(db.Model):

    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255)
    product_description = CharField(max_length=255)
    product_cost = DoubleField()
    product_discontinued = IntegerField(default=0)

    class Meta:
        database = db
        table_name = 'Product'
