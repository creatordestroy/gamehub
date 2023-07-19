from datetime import datetime
from item import Item
import os
import json

class OrderForm(object):

    def __init__(self):
        self.name = "orderform.json"
        self.date = datetime.today()
        self.check_orderform(self.name)

    """
    Description: Adds a product to the order form
    Parameters: Item -> item to be added, quantity -> quantity to be ordered as an integer, default 5
    Return Value: None
    """
    def add_to_order(self, item: Item, quantity: int=5) -> None:
        print("adding item to orderform...")
        with open("orderform.json",'r') as orderform:
            order_info = orderform.read()
            order_data = json.loads(order_info)
            orderform.close()

        order_data[item.sku] = item.__dict__
        item.updateQuantity(quantity)

        with open("orderform.json", 'w') as orderform:
            updated_form = json.dumps(order_data)
            orderform.write(updated_form)
            orderform.close()

    """
    Description: Checks if orderform.json exists, if it does not, creates orderform.json
    Parameters: name -> filename as a string
    Return Value: None
    """
    def check_orderform(self,name: str) -> None:
        if os.path.exists(name):
            print("orderform.json exists already")
        else:
            print("Creating new json order file...")
            base_data = {}

            with open(name, 'w') as orderform:
                inv_data = json.dumps(base_data)
                orderform.write(inv_data)
                orderform.close()

    """
    Description: Removes all current items in the orderform
    Parameters: None
    Return Value: None
    """
    def clear_order(self) -> None:
        print("clearing orderform...")
        with open("orderform.json", 'r') as orderform:
            inv_info = orderform.read()
            inv_data = json.loads(inv_info)
            orderform.close()

        inv_data = {}
        with open("orderform.json", 'w') as orderform:
            new_data = json.dumps(inv_data)
            orderform.write(new_data)
            orderform.close()


