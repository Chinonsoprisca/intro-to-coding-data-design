"""
Exercise 1:
Extend the program from last week to convert the temperature from Fahrenheit
to Celsius.
1. Ask the user for the name of a city and the current temperature in Fahrenheit.
2. Convert the temperature to Celsius.
3. If the temperature is below freezing point (0 °C),
    print a warning message saying "Alert: The temperature is below freezing point."
Otherwise, print a message saying
    "The temperature is above the freezing point."
4. Lastly, always print the temperature in Celsius (up to one decimal point).
PS:
The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9

Example output 1:
Enter the name of a city: Munich
Enter the current temperature in Farenheit: 60
The temperature is above the freezing point.
The current temperature in Munich is 15.6 degrees Celsius.

Example output 2:
Enter the name of a city: Munich
Enter the current temperature in Farenheit: 25
Alert: The temperature is below freezing point.
The current temperature in Munich is -3.9 degrees Celsius.
"""


# Exercise 1 Solution:

# Ask the user for the city name
city = input("Enter the name of a city: ")

# Ask the user for the current temperature in Fahrenheit
temp = input("Enter the current temperature in Fahrenheit: ")

# Convert the temperature to float
temp_in_f = float(temp)

# Convert the temperature to Celsius
temp_in_c = (temp_in_f - 32) * 5/9

# Check if the temperature is below freezing point
if temp_in_c < 0:
    print("Alert: The temperature is below freezing point.")
else:
    print("The temperature is above the freezing point.")

# Print the user input in a formatted string
print(f"The current temperature in {city} is {temp_in_c} degrees Celcious.")