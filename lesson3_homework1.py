"""Exercise 1
Improve your program from last week to handle multiple cities. The user should
be able to enter the names and temperatures of as many cities as they want. Use
a loop to facilitate this and print out all the cities along with
their temperatures in Celsius and Fahrenheit. Again, give a warning if the
temperature is below the freezing point. To stop the loop, the user should
be able to enter "exit" as the city name.
Example output:
Please enter the name of a city: Munich
Please enter the current temperature in Farenheit in Munich: 14
The current temperature in Munich is 14°F or -10°C.
Warning: The temperature is below freezing point.

Please enter the name of a city: exit
"""

# Exercise 1 solution

# Ask the user for the current temperature in Fahrenheit
print("INSTRUCTION: Please type 'exit' to end, or enter a city name to proceed.")
city = input("Please enter the name of a city: ")

while city != "exit":
    temp_f = float(input(f"Enter the current temperature in {city} in Fahrenheit: "))  
    temp_c = (temp_f - 32) * 5/9       # Convert the temperature to Celsius
    print(f"The current temperature in {city} is {temp_c:.1f}°C or {temp_f:.1f}°F")    # formatted string
    # Check if the temperature is below freezing point
    if temp_c < 0:
        print("Alert: The temperature is below freezing point.")
    else:
        print("The temperature is above the freezing point.")   
    # Ask the user for the city name
    city = input("Please enter the name of another city (or enter exit to quit): ")
