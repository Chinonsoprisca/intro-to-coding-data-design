"""Exercise 5
Write a program that takes a list of numbers as input and prints the largest
and smallest numbers in the list.
numbers = [12, 3, 5, 19, 7, 3, 1, 5]

Example output:
The largest number is 19.
The smallest number is 1.
"""
# Exercise 5 solution
numbers = [12, 3, 5, 19, 7, 3, 1, 5]

largest = None
smallest = None
for number in numbers:
    if largest is None:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
print(f"The largest number is {largest}.")
print(f"The smallest number is {smallest}.")