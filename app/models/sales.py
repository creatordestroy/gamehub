from peewee import *
from app.database import db
from app.models.inventory import Inventory
from app.models.user import User

class Sales(db.Model):

    sales_id = PrimaryKeyField
    product_id = ForeignKeyField(Inventory, backref="Sales")
    user_id = ForeignKeyField(User, backref="Sales")
    sale_date = DateField()
    sale_quantity = IntegerField()
    sale_amount = DecimalField()

class Meta:
    database = db