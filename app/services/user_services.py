from app.models.user import User
from app.models.wishlist import WishList

class UserService:
    def add_user(username, password, role):
        user = User(username=username, password=password, role=role)
        user.save()

    def get_user(username):
        return User().get(User().username == username)

    def add_to_wishlist(user_id, inventory_id):
        wishlist_item = WishList(user_id=user_id, inventory_id=inventory_id)
        wishlist_item.save()
