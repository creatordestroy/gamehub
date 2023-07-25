from app.models.inventory import Inventory
from app.models.user import User
from app.models.wishlist import WishList

class WishlistServices:
    def add_to_wishlist(self, user_id, product_id, date_added):
        if not user_id:
            # return "<h1>Please login to continue</h1>"
            user_id = User.select()[0].user_id
        wishlist_item = WishList(user_id=user_id, product_id=product_id, date_added=date_added)
        wishlist_item.save()
        return wishlist_item

    def wishlist(user_id):
        if not user_id:
            # return "<h1>Please login to continue</h1>"
            user_id = User.select()[0].user_id
        return WishList.select().where(WishList.user_id_id == user_id)

    def get_wishlist(user_id):
        if not user_id:
            # return "<h1>Please login to continue</h1>"
            user_id = User.select()[0].user_id
        return [i.product_id_id for i in WishList.select().where(WishList.user_id_id == user_id)]
