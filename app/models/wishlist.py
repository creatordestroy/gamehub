from peewee import *
from app.models.user import User
from app.models.inventory import Inventory
from app.database import db

class WishList(db.Model):
    
    __tablename__ = 'Wishlist'
    wishlist_id = PrimaryKeyField()
    user_id = ForeignKeyField(User, backref='Wishlist')
    product_id = ForeignKeyField(Inventory, backref='Wishlist')
    date_added = DateField()

    class Meta:
        database = db