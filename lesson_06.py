import requests

""" Exercise 1

 Create a function that greets a list of persons.
 The function should take two arguments names_list and greeting_text. 
 Inside the function create a for-loop which iterates over 
 the names and prints out the greeting of your choice
 """
# names_list = ["Maria", "Olabisi", "Ronah", "Olubukola"]
# greeting_text = "Hello, "

# Function to greet a list of people:
def greet_people(names_list, greeting_text):
  for name in names_list:
    print(f"{greeting_text}{name}")

greet_people(["Maria", "Olabisi", "Ronah", "Olubukola"], "Hello, ")
greet_people(["Maria", "Olabisi", "Ronah", "Olubukola"], "Good morning, ")
greet_people(["Maria", "Olabisi", "Ronah", "Olubukola"], "Good day, ")


# Function to greet people based on familiarity
def greet_people_special(names_list, greeting_text_standard, greeting_text_casual, greeting_text_formal):
  for name in names_list:
    if (name == "Maria"):
      print(f"{greeting_text_casual}{name}")
    elif (name == "Olabisi"):
      print(f"{greeting_text_formal}{name}")
    else:
      print(f"{greeting_text_standard}{name}")

greet_people_special(["Elissavet", "Noorina", "Chinonso", "Queensly"], "Hello ", "Wassup, ", "Good day to you, miss ")


# -------------------------------------------------------------------------- 
""" Exercise 3

Area Calculator: Define functions for calculating the area of a circle, square,
and triangle. Prompt the user to choose a shape and input the necessary parameters 
 to calculate and display the area.
 The area of a circle is calculated as follows: area = pi * radius * radius
 The area of a square is calculated as follows: area = length * length
 The area of a triangle is calculated as follows: area = 0.5 * base * height """

# Solution

# This function calculates the circle area
def calculate_area_circle():
  radius = float(input("What's the circle radius?"))
  area = 3.14 * radius * radius
  return area

# This function calculates the square area
def calculate_area_square():
  length = float(input("What's the length of the square side?"))
  area = length * length
  return area

# This function calculates the triangle area
def calculate_area_triangle():
  base = float(input("What's the triangle base?"))
  height = float(input("What's the triangle height?"))
  area = 0.5 * base * height
  return area

def calculate_area(shape):
  if (shape == "circle"):
    return calculate_area_circle()
  elif (shape == "square"):
    return calculate_area_square()
  elif (shape == "triangle"):
    return calculate_area_triangle()
  else: 
    print("I need a proper shape!")
    return None

shape_choice = input("Which shape are you calculating the area for? (circle/square/triangle)")
print(calculate_area(shape_choice))


# -----------------------------------------------------------------

# exploratory exercise
def my_func(list):
  list.append("Noor")
  list.remove("Olabisi")

first_list = ["Maria", "Olabisi", "Ronah", "Olubukola"]
my_func(first_list)
print(first_list)

second_list = ["Elissavet", "Noorina", "Chinonso", "Queensly"]
my_func(second_list)
print(second_list)


# -----------------------------------------------------------------
# random library
import random
random_nbrs = []
for i in range(10):
    random_nbrs.append(random.randint(1, 100))
    print(random_nbrs)


# --------------------------------------------------------------

""" Exercise 4:
Making an API call: Use the requests library to make a call to the following API:
https://geocoding-api.open-meteo.com/v1/search?name=munich&count=1&language=en&format=json
An API call is like a url. You can open it in your browser and see the result.

1. Install the requests library using pip install requests
2. Import the requests library
3. Define a variable url with the url above as a string
4. Make the call using response = requests.get(url)
5. Convert the result to json using response.json()
6. Print the result
7. What kind of data structure is the result? What does it contain?
8. How can you access the latitude, longitude and elevation of the city? Print it
 """

# Solution

url = "https://geocoding-api.open-meteo.com/v1/search?name=munich&count=1&language=en&format=json"

response = requests.get(url)
print(response)
print(response.json())


# --------------------------------------------------------------------



# requests library

city_name = input("Please enter the city")
api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"

# The response from the API
api_response = requests.get(url = api_url) # the function we use from requests

# Converts the response from the API to the dictionary
api_response_json = api_response.json() # 

# Parse the response to get the required information
#print(f'The response from the API: {api_response_json}')

all_results = api_response_json["results"]
#print(f'All the results: {all_results}')

city_result = all_results[0]
print(f'The first result: {city_result}')

city_population = city_result["population"]
city_name = city_result["name"]

print(f'The population of {city_name}: {city_population}')

print(f'The latitude in {city_name}: {city_result["latitude"]}')
print(f'The longitude in {city_name}: {city_result["longitude"]}')
print(f'The elevation in {city_name}: {city_result["elevation"]}')
