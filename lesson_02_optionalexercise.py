"""
Exercise 5: Grade Classification
Instruction:

Ask the user to enter a numeric grade (0 to 100) using input().
Convert the input to an integer and classify the grade as follows:
90 or above: "A"
80 to 89: "B"
70 to 79: "C"
60 to 69: "D"
Below 60: "F"
Print the grade classification.
"""

# Exercise 5 solution:

grade_input = input("Enter a numeric grade that is between 0 and 100: ")
grade = int(grade_input)
if grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")

    
"""
Exercise 6: Ticket Price
Instruction:

Ask the user to enter their age using input().
Convert the input to an integer and determine the ticket price based on age:
0 to 3 years: Free
4 to 12 years: $10
13 to 64 years: $15
65 and above: $5
Print the ticket price.
"""

# Exercise 6 Solutions:

age_input = input("Please enter your age: ")
age = int(age_input)
if age <= 3:
    print("Ticket is Free")
elif age <= 12:
    print("Ticket costs $10")
elif age <= 64:
    print("Ticket costs $15")
else:
    print("Ticket costs $5")

"""
Exercise 7: Logical Combinations
Instruction:

Ask the user to enter an integer using input().
Convert the input to an integer and check if it's between 10 and 50 (inclusive) or less than 0.
Print the result of the condition.
"""
# Exercise 7 Solution:

integer = input("Please enter an integer: ")
number = int(integer)
if number >= 10 and number <= 50:
    print("The number is between 10 and 50")
elif number < 0:
    print("The number is less than 0")
else:
    print("The number is neither between 10 and 50 nor less than 0: ")


"""
Exercise 8:
Enhance the code below, so that when a user wants anything else besides coffee or tea you inform the user 
that the required beverage is not available:
print("Turning on the machine...")
beverage = input("Do you want tea or coffee? ")
if beverage == "tea":
    print("Preparing tea...")
elif beverage == "coffee" :
    print("Preparing coffee...")
print("Turning off the machine.")
"""

# Exercise 8 Solutions:

print("Turning on the machine...")
beverage = input("Do you want tea or coffee? ")
if beverage == "tea":
    print("Preparing tea...")
elif beverage == "coffee" :
    print("Preparing coffee...")
else:
    print("Required beverage is not available")
print("Turning off the machine.")
