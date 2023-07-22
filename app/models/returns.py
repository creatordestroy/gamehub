from peewee import *
from app.database import db
from app.models.storeLocation import StoreLocation
from app.models.product import Product

class Returns(db.Model):

    return_id = PrimaryKeyField()
    store_id = ForeignKeyField(StoreLocation, backref="Returns")
    user_id = ForeignKeyField(Product, backref="Returns")
    return_date = DateField()
    return_reason = CharField()

    class Meta:
        database = db
        table_name = 'Returns'