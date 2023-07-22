from peewee import *
from app.database import db
from app.models.product import Product
from app.models.user import User

class Reviews(db.Model):

    review_id = PrimaryKeyField()
    product_id = ForeignKeyField(Product, backref='Reviews')
    user_id = ForeignKeyField(User, backref='Reviews')
    product_rating = DoubleField()
    product_review = CharField()
    review_date = DateField()

    class Meta:
        database = db
        table_name = 'Reviews'