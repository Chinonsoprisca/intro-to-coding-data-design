"""Exercise 2
1. Create a list of your favorite fruits. Print the third fruit on the list.
2. Append two new fruits to your favorite fruits. Print the updated list
3. Remove the second fruit from the list and print the updated list.
"""

# Exercise 2 solution
fruits = ["Cherry", "Apple", "Banana", "Avocado"]
print(fruits[2])
fruits.extend(["Orange", "Pear"])
print(fruits)
fruits.pop(1)
print(fruits)
