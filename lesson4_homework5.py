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

max = None
min = None
for number in numbers:
    if max is None:
        max = number
        min = number
    else:
        if number > max:
            max = number
        if number < min:
            min = number
print(f"The largest number is {max}.")
print(f"The smallest number is {min}.")