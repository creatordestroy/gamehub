from peewee import *
from app.database import db

class StoreLocations(db.Model):

    #__tablename__ = 'StoreLocations'
    store_id = PrimaryKeyField()
    location_name = CharField(max_length=255)
    location_address = CharField(max_length=255)
    
    class Meta:
        database = db