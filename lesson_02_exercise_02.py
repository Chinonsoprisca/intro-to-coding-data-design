"""
Exercise 2:
Now extend the program and ask for the temperature in two cities.
1. Ask the user for the name of two cities and the current temperatures in Fahrenheit.
2. Convert the temperatures to Celsius.
3. If the temperature in both cities is below freezing point (32 °F),
    print a warning message saying "Alert: The temperatures in both cities are below freezing point."
else if the temperature in only one of the cities is below freezing point,
    print a warning message saying "Alert: The temperature in one of the cities is below freezing point."
Otherwise, print a message saying
    "The temperatures in both cities are above the freezing point."
4. Lastly, always print the temperatures in Celsius (up to one decimal point).
PS:
The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9

Example output 1 (both cities below freezing point):
Enter the name of the first city: Munich
Enter the name of the second city: Paris
Please enter the current temperature for Munich in Farenheit: 15
Please enter the current temperature for Paris in Farenheit: 10
Alert: The temperatures in both cities are below freezing point.
The current temperature in Munich is -9.4 degrees Celsius.
The current temperature in Paris is -12.2 degrees Celsius.

Example output 2 (one city below freezing point):
Enter the name of the first city: Munich
Enter the name of the second city: Paris
Please enter the current temperature for Munich in Farenheit: 40
Please enter the current temperature for Paris in Farenheit: 30
Alert: The temperature in one of the cities is below freezing point.
The current temperature in Munich is 4.4 degrees Celsius.
The current temperature in Paris is -1.1 degrees Celsius.

Example output 3 (both cities above freezing point):
Enter the name of the first city: Munich
Enter the name of the second city: Paris
Please enter the current temperature for Munich in Farenheit: 40
Please enter the current temperature for Paris in Farenheit: 50
The temperatures in both cities are above the freezing point.
The current temperature in Munich is 4.4 degrees Celsius.
The current temperature in Paris is 10.0 degrees Celsius.
"""


# Exercise 2 solution:

# Ask the user for the city names
city1 = input("Enter the name of the first city: ")
city2 = input("Enter the name of the second city: ")

# Ask the user for the current temperatures in Fahrenheit
temp_1 = input(f"Please enter the current temperature in {city1} in Fahrenheit: ")
temp_2 = input(f"please enter the current temperature in {city2} in Fahrenheit: ")

# Convert the temperatures to float
temp1_f = float(temp_1)
temp2_f = float(temp_2)

# Convert the temperature to Celsius
temp1_c = (temp1_f - 32) * 5/9
temp2_c = (temp2_f - 32) * 5/9

# Check if the temperature is below freezing point
if temp1_f and temp2_f < 32:
    print("Alert: The temperatures in both cities are below freezing point.")
elif temp1_f or temp2_f < 32:
    print("Alert: The temperature in one of the cities is below freezing point.")
else:
    print("The temperatures in both cities are above the freezing point.")

# Print the user input in a formatted string
print(f"The current temperature in {city1} is {temp1_c:.1f} in degrees Celcious.")
print(f"The current temperature in {city2} is {temp2_c:.1f} degrees Celcious")

# Please Note: AI didn't write my code, I only used it to figure out how to reduce
# my float output from 9 decimal places to 1 decimal place i.e {temp1_c:.2f} . 