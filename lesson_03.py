# Python loop (while loop and for loop)

# Exercise 1 solution with: while loop

chapter = 0
while chapter < 10:
    page = 0
    while page < 20:
        print(f"Chapter {chapter} Page {page}")
        page += 1
    print(f"Finished Chapter {chapter}")
    chapter += 1


# Exercise 1 solution with: for loop 
for chapter in range (10):
    for page in range (20):
        print(f"Chapter {chapter} Page {page}")
    print(f"Finished Chapter {chapter}")


""" Exercise 2:
Write a program that calculates and prints the sum of all numbers from 1 to a
user-specified positive integer.  
Example output:
Enter a positive integer: 5
Sum: 15

Array: 1, 2, 3, 4, 5
Output is Sum = 1 + 2 + 3 + 4 + 5 """

# Exercise 2 solution with: while loop

value = 1
max_value = int(input("Enter a positive integer number: "))
sum = 0
while value <= max_value:
    sum = sum + value
    print(f"value = {value} sum = {sum}")
    value += 1
print(f"Final Sum = {sum}") 


# Exercise 2 solution with: for loop

max_value = int(input("Enter a positive integer number: "))
sum = 0
for value in range(1,max_value + 1):
    sum = sum + value
    print(f"value = {value} sum = {sum}")
print(f"Final Sum = {sum}")


# more examples for the "for loops"   
# 1.

fruits = ['apples', 'oranges', 'bananas', 'kiwi']

# sequence is fruits
# variable fruit

for fruit in fruits:
  # fruit = apples ➡️ oranges ➡️ bananas
  print(fruit)

# output:

# apples
# oranges
# bananas
# kiwi

# 2.