from peewee import *
from app.models.user import User
from app.models.product import Product
from app.database import db

class WishList(db.Model):
    
    wishlist_id = PrimaryKeyField()
    user_id = ForeignKeyField(User, backref='Wishlist')
    product_id = ForeignKeyField(Product, backref='Wishlist')
    date_added = DateField()

    class Meta:
        database = db
        table_name = 'Wishlist'