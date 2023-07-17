from datetime import datetime
from item import Item
import os
import json

class OrderForm(object):

    def __init__(self):
        self.name = "orderform.json"
        self.date = datetime.today()
        self.check_orderform(self.name)


    def add_to_order(self, item: Item, quantity: int=5) -> None:
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

    def check_orderform(self,name) -> None:
        if os.path.exists(name):
            print("orderform.json exists already")
        else:
            print("Creating new json order file...")
            base_data = {}

            with open(name, 'w') as orderform:
                inv_data = json.dumps(base_data)
            orderform.write(inv_data)
            orderform.close()

    def clear_order(self) -> None:
        with open("orderform.json", 'r') as orderform:
            inv_info = orderform.read()
            inv_data = json.loads(inv_info)
            orderform.close()

        inv_data = {}
        with open("data.json", 'w') as orderform:
            new_data = json.dumps(inv_data)
            orderform.write(new_data)
            orderform.close()


