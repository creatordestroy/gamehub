from peewee import *
from app.models.user import User
from app.models.inventory import Inventory
from app.database import db

class WishList(db.Model):
    
    __tablename__ = 'Wishlist'
    wishlist_id = db.Column(db.Integer, primaryKey = True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    product_id = db.Column(db.Integer, db.ForeignKey(Inventory.product_id))
    date_added = db.Column(db.Date, nullable = False)

    class Meta:
        database = db