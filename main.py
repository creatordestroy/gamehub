import json
from item import Item
import pandas as pd


def main():
    
    #populateInventory()
    #new_item = Item("xbox","1001",499.99,5)
    #addItem(new_item, new_item.sku)
    #removeItem(new_item)
    #printInventory()
    clearInventory()

    return 0

"""
Description: Function populates json file with original available products
Parameters: None
Return Value: None
"""
def populateInventory() -> None:
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
def addItem(item: Item) -> None:
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
def removeItem(item: Item) -> None:
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
def printInventory() -> None:
    with open('data.json', 'r') as inventory:
        inv_data = json.load(inventory)
        inventory.close()
        print(inv_data)

"""
Description: Function removes all existing products from the database
Parameters: None
Return Value: None
"""
def clearInventory() -> None:

    with open("data.json", 'r') as inventory:
        inv_info = inventory.read()
        inv_data = json.loads(inv_info)
        inventory.close()

    inv_data = {}
    with open("data.json", 'w') as inventory:
        new_data = json.dumps(inv_data)
        inventory.write(new_data)
        inventory.close()

if __name__ == "__main__":
    main()