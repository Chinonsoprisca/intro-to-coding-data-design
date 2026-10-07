""" Add a new functionality to your program from exercise 1.
After the program is finished, print a summary containing the highest and lowest
temperatures in degrees Celcius and the corresponding city names.

Example output:
Please enter the name of a city: Munich
Please enter the current temperature in Fahrenheit in Munich: 14
The current temperature in Munich is 14°F or -10°C.
Warning: The temperature is below freezing point.

Please enter the name of a city: Berlin
Please enter the current temperature in Fahrenheit in Berlin: 100
The current temperature in Berlin is 100°F or 37.7°C.

Please enter the name of a city: Hamburg
Please enter the current temperature in Fahrenheit in Hamburg: 0
The current temperature in Berlin is 0°F or -17.8°C.

Please enter the name of a city: exit

Summary:
The highest temperature is 37.7°C in Berlin.
The lowest temperature is -17.8°C in Hamburg. """

# Exercise 2 soulution
print("INSTRUCTION: Please type 'exit' to end, or enter a city name to proceed.")
city = input("Please enter the name of a city: ")
highest_temp = None
lowest_temp = None
highest_temp_city = None
lowest_temp_city = None

while city != "exit":
    temp_f = float(input(f"Enter the current temperature in {city} in Fahrenheit: "))  
    temp_c = (temp_f - 32) * 5/9       # Convert the temperature to Celsius
    print(f"The current temperature in {city} is {temp_c:.1f}°C or {temp_f:.1f}°F")    # formatted string
    
    # Check if the temperature is below freezing point
    if temp_c < 0:
        print("Alert: The temperature is below freezing point.")
    else:
        print("The temperature is above the freezing point.")

    # compare the temparatures for the highest and lowest
    if highest_temp is None:
        highest_temp = temp_c
        lowest_temp = temp_c 
        highest_temp_city = city
        lowest_temp_city = city 
    if temp_c >= highest_temp:
        highest_temp = temp_c
        highest_temp_city = city
    if temp_c <= lowest_temp:
        lowest_temp = temp_c
        lowest_temp_city = city
    # Ask the user for the city name
    city = input("Please enter the name of another city (or enter exit to quit): ")
    print("Summary:")
    print(F"The highest temperature is {highest_temp:.1f}°C in {highest_temp_city}.")
    print(F"The lowest temperature is {lowest_temp:.1f} in {lowest_temp_city}.")
else:
    print("Thank you")
