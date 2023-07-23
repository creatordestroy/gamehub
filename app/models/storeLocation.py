from peewee import *
from app.database import db

class StoreLocation(db.Model):

    store_id = PrimaryKeyField()
    store_name = CharField(max_length=255)
    store_address = CharField(max_length=255)

    class Meta:
        database = db
        table_name = 'StoreLocation'