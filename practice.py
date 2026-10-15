
""" Write a program that simulates a simple inventory system. Create a dictionary
with items as keys and their quantities as values. Allow the user to "buy"
items by reducing the quantity, and print the updated inventory after each
purchase.

inventory = {
    "apple": 5,
    "banana": 3,
    "orange": 2,
    "pear": 1
}
Example output:
Please enter the name of an item to buy: apple
There are 4 apples left in stock.
Please enter the name of an item to buy: pear
There are 0 pears left in stock.
Please enter the name of an item to buy: pear
Sorry, there are no pears left in stock.
Please enter the name of an item to buy: exit
 """

print("Avalaible items include: apple, banana, orange, pear")

inventory = {
    "apple": 5,
    "banana": 3,
    "orange": 2,
    "pear": 1
}

while True:
    item = input("Please enter an item you want to buy or enter exit: ")
    if item == "exit":
        break
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        print(f"There are {inventory[item]} {item} left in stock")
    else:
        print(f"Sorry! there are no {item} left in stock.")
    if item not in inventory:
        print("Sorry! item is not avaible")