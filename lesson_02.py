#Exercise 1: Simple Comparison
#Ask the user to enter two numbers (num1 and num2) using input().
#Convert the input to integers and compare if num1 is greater than num2.
#Print the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if  num1>num2:
    print("first number is greater than second number")
elif num1<num2:
    print("first number is less than second number")
else:
    print("first number is equal to second number")
 

#Exercise 2: String Comparison:
#Ask a user to enter their name. If the name has 6 characters or more, inform the user that they have a long name.

name = input("Enter your name: ")
if len(name) > 6:
    print("you have a long name")
elif len(name) == 6:
    print("you have a medium name")
else:
    print("you have a short name")


""" Exercise 3: Even or Odd (rooms 1 and 2)
Ask the user to enter an integer using input(). Convert the input to an integer and determine if it's even or odd.
Print the result.
"""

integer_number = input("Enter an integer: ")
integer = int(integer_number)
if integer%2 == 1:    #use modulus to determine numbers that are odd or even
    print("integer is odd number")
else:
    print("integer is even number")


""" Exercise 4: Password Check (rooms 3 and 4)
Set a password (e.g., "python123") as a string. Ask the user to enter a password using input().
Compare the user's input with the actual password and check if they match.
Print "Access Granted" if the password is correct; otherwise, print "Access Denied". 
 """
password = "python123"
password_input = input("Enter password: ")
if password_input == password:
    print("Access Granted")
else:
    print("Acsess Denied")