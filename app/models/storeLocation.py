from peewee import *
from app.database import db

class StoreLocation(db.Model):

    store_id = PrimaryKeyField()
    location_name = CharField(max_length=255)
    location_address = CharField(max_length=255)
    
    class Meta:
        database = db
        table_name = 'StoreLocation'