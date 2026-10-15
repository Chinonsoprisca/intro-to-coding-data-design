"""Exercise 1

Improve your weather forecast program to handle multiple cities ad more information.

All cities should be stored in a dictionary. The city name should be the key
and the value should be another dictionary containing the following information:
- current temperature in Celsius
- current temperature in Fahrenheit
- is it raining? ("yes" or "no")
- is the sun shining? ("yes" or "no")

The user should be able to finish the program by entering "exit" as city name

Once the user is finished, print a summary for each city with the information above.
If the temperature is below 0°C, print a warning message.
If it is both raining and the sun is shining, print a notification that there is a rainbow.


Example output:
Please enter the name of a city: Munich
Would you like to enter the temperature in Fahrenheit or Celsius?: Celsius
Please enter the current temperature in Celsius in Munich: 14
Is it raining in Munich? (yes/no): no
Is the sun shining in Munich? (yes/no): yes

Please enter the name of a city: Berlin
Would you like to enter the temperature in Fahrenheit or Celsius?: Fahrenheit
Please enter the current temperature in Fahrenheit in Berlin: 34
Is it raining in Berlin? (yes/no): yes
Is the sun shining in Berlin? (yes/no): yes

Please enter the name of a city: Hamburg
Would you like to enter the temperature in Fahrenheit or Celsius?: Celsius
Please enter the current temperature in Celsius in Hamburg: 5
Is it raining in Hamburg? (yes/no): yes
Is the sun shining in Hamburg? (yes/no): no

Please enter the name of a city: exit

Summary:
Munich: 14°C, 57°F, sun and no rain

Berlin: 1°C, 34°F, sun and rain,
Warning: The temperature in Berlin is below the freezing point
There is a rainbow in Berlin.

Hamburg: 5°C, 41°F, no sun and rain
"""

# Exercise 1 solution

cities = {}

while True:
    city = input("Please enter the name of a city to continue or enter exit to stop: ").capitalize()
    if city.lower() == "exit":
        break
    temp_in_f = None
    temp_in_c = None
    rain = None
    sun = None
    temp_choice = input("Would you like to enter the temperature in Fahrenheit or Celsius?: ").capitalize()
    if temp_choice == "Fahrenheit":
        temp_in_f = float(input(f"Please enter the current temperature in Fahrenheit in {city}: "))
        temp_in_c = (temp_in_f - 32) * 5 / 9
    if temp_choice == "Celsius":
        temp_in_c = float(input(f"Please enter the current temperature in Celsius in {city}: "))
        temp_in_f = (temp_in_c * 9 / 5) + 32
    rain = input("Is it raining? Please enter yes or no: ").lower()
    if rain == "yes":
        rain = "rain"
    else:
        rain = "no rain"
    sun = input(" Is the sun shining? Please enter yes or no: ").lower()
    if sun == "yes":
        sun = "sun"
    else:
        sun = "no sun"
    cities[city] = {
        "temp_in_c": temp_in_c,
        "temp_in_f": temp_in_f,
        "rain": rain,
        "sun": sun
    }
if cities != {}:
    print("Summary:")
for city, values in cities.items():
    print(f"{city}: {values["temp_in_c"]:.1f}°C, {values["temp_in_f"]:.1f}°F, {values["sun"]} and {values["rain"]}")

    if values["temp_in_c"] < 0:
        print(f"Warning: The temperature in {city} is below the freezing point")
    if values["sun"] == "sun" and values["rain"] == "rain":
        print(f"There is a rainbow in {city}")
