import json
import os
from item import Item

class Inventory(object):

    def __init__(self, dB_name: str):
        self.dB_name = "data.json"
        self.check_for_db(self.dB_name)

    """
    Description: Function populates json file with original available products
    Parameters: None
    Return Value: None
    """
    def populateInventory(self) -> None:
        print("Populating database...")
        products = {1000: {"name" : "ps4", "sku" : "1000", "cost" : 350.99,
                                    "stock" : 4}}
        product_data = json.dumps(products)
        inv_file = open("data.json", 'w')
        inv_file.write(product_data)
        inv_file.close()

    """
    Description: Adds a new product to the existing inventory
    Parameters: item: An item object to be added
    Return Value: None
    """
    def addItem(self, item: Item) -> None:
        print("Adding new item to data.json...")
        with open("data.json", 'r') as inventory:
            inv_info = inventory.read()
            inv_data = json.loads(inv_info)
            inventory.close()
        inv_data[item.sku] = item.__dict__
        with open("data.json" , 'w') as inventory:
            new_data = json.dumps(inv_data)
            inventory.write(new_data)
            inventory.close()

    """
    Description: Removes an existing product from the inventory
    Parameters: Item to be removed
    Return Value: None
    """
    def removeItem(self, item: Item) -> None:
        print("Removing item from data.json...")
        with open('data.json', 'r') as inventory:
            inv_info = inventory.read()
            inv_data = json.loads(inv_info)
            inventory.close()

        if inv_data[item.sku]:
            inv_data.pop(item.sku)

        with open('data.json', 'w') as inventory:
            new_data = json.dumps(inv_data)
            inventory.write(new_data)
            inventory.close()

    """
    Description: Prints the existing contents of the inventory to the console
    Parameters: None
    Return Value: None
    """
    def printInventory(self) -> None:
        print("Current inventory: ")
        with open('data.json', 'r') as inventory:
            inv_data = json.load(inventory)
            inventory.close()
            print(inv_data)

    """
    Description: Function removes all existing products from the database
    Parameters: None
    Return Value: None
    """
    def clearInventory(self) -> None:

        with open("data.json", 'r') as inventory:
            inv_info = inventory.read()
            inv_data = json.loads(inv_info)
            inventory.close()

        inv_data = {}
        with open("data.json", 'w') as inventory:
            new_data = json.dumps(inv_data)
            inventory.write(new_data)
            inventory.close()

    def check_for_db(self, name: str) -> None:
        if os.path.exists(name):
            print("Data.json exists already")
        else:
            print("Creating new json database file...")
            base_data = {}

            with open(name, 'w') as inventory:
                inv_data = json.dumps(base_data)
                inventory.write(inv_data)
                inventory.close()