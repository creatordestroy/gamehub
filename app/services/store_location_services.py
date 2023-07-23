from app.models.storeLocation import StoreLocation

class StoreLocationService:
    def get_store_location_list(self):
        return StoreLocation.select()
