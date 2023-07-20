from peewee import *
from app.database import db

class StoreLocations(db.Model):

    __tablename__ = 'StoreLocations'
    store_id = db.Column(db.Integer, primaryKey = True)
    location_name = db.Column(db.varchar(255), nullable = False)
    location_address = db.Column(db.varchar(255), nullable = False)
    

    class Meta:
        database = db