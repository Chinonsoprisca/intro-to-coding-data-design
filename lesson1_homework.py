"""
Exercise 1:
Create a program that
1. asks the user to enter the name of a city and the current
temperature in Celsius.
2. Store the user input in separate variables and
3. display them.
PS:
Use type conversion to ensure that the user's input for the temperature is treated as a float.
Example output:
Please enter the name of a city: Munich
Please enter the current temperature in Celsius in Munich: 25.5
The current temperature in Munich is 25.5 degrees Celsius.
"""
# Ask the user for the city name
# Ask the user for the current temperature in Celsius
# Convert the temperature to float
# Print the user input in a formatted string

# Exercise 1 Solution:
city = input("Please enter the name of a city: ")
temperature = float(input(f"Please enter the current temperature in Celsius in {city}: "))
print(f"The current temperature in {city} is {temperature} degrees Celcius")



"""
Exercise 2:
Now create a program that asks the user to enter the name of two cities and the
current temperatures in each city in Celsius. Store the user inputs in separate
variables (two variables for the names and two for the temperatures) and
display the average temperature.
Example output:
Please enter the name of the first city: Munich
Please enter the name of the second city: Paris
Please enter the current temperature for Munich: 25.5
Please enter the current temperature for Paris: 11.5
The average temperature between Munich and Paris is 18.5 degrees Celsius.
"""
# Ask the user for the city names
# Ask the user for the current temperatures in Celsius
# Convert the temperatures to float
# Calculate the average temperature
# Print the user input in a formatted string

# Exercise 2 Solution:
city1 = input("Please enter the name of the first city: ")
city2 = input("Please enter the name of the second city: ")
temperature1 = float(input(f"Please enter the current temperature for {city1}: "))
temperature2 = float(input(f"Please enter the current temperature for {city2}: "))
Average = (temperature1+temperature2)/2
print(f"The average temperature between {city1} and {city2} is {Average} degree Celcious")



"""
Exercise 3:
Building upon exercise 2, also convert and print the average temperature in
Fahrenheit. The formula for converting Celsius to Fahrenheit is: F = C * 9/5 + 32.
Example output:
Please enter the name of the first city: Munich
Please enter the name of the second city: Paris
Please enter the current temperature for Munich: 25.5
Please enter the current temperature for Paris: 11.5
The average temperature between Munich and Paris is 18.5 degrees Celsius.
That's 65.3 degrees Fahrenheit.
"""
# Ask the user for the city names
# Ask the user for the current temperatures in Celsius
# Convert the temperatures to float
# Calculate the average temperature
# Print the user input in a formatted string
# Convert the average temperature to Fahrenheit


# Exercise 3 Solution:
city1 = input("Please enter the name of the first city: ")
city2 = input("Please enter the name of the second city: ")
temperature1 = float(input(f"Please enter the current temperature for {city1}: "))
temperature2 = float(input(f"Please enter the current temperature for {city2}: "))
Average = (temperature1+temperature2)/2
print(f"The average temperature between {city1} and {city2} is {Average} degree Celcious")
fahrenheit = Average * 9/5 + 32
print(f"That is {fahrenheit} degrees Fahrenheit")

