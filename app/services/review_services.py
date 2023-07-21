from app.models.inventory import Inventory
from app.models.user import User
from app.models.reviews import Reviews
from flask import jsonify
from app.database import db

class ReviewService:

    def get_all_product_reviews():
        try:
            product_reviews = Reviews.select()

            if product_reviews:

                reviews_data = [review.__data__ for review in product_reviews]

                return {'message': 'Successfully retrieved test product', 'product_data': reviews_data}, 200
            else:
                return {'message': 'No products found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500