# DICTIONARIES

# create a dictionary about yourself, that uses name, hobby and home-country
# as key and put in the values for yourself.
#print the dictionary

#my_dic = {"name"}
#print (my_dic.values())

""" Exercise 1
Create a dictionary about yourself, that uses name, hobby and home-country as key, and put in the values for yourself. Print the dictionary

Exercise 2
Use this dictionary:
luggage = {
    'bag': ['smartphone', 'chewing gum', 'wallet'],
    'backpack': ['laptop', 'notepad', 'sandwich', 'energy drink']
}
1 Add a key called pocket, and set its value to integer 50
2 Sort the items in the backpack key
	Start with:
  Backpack = luggage[“backpack”]
3 Remove sandwich from the list of items under the backpack key
4 Add 10 to the number stored under the key pocket """

# solution

luggage = {
    "bag": ["smartphone", "chewing gum", "wallet"],
    "backpack": ["laptop", "notepad", "sandwich", "energy drink"]
    }

luggage["pocket"] = 50   # int(50)
print(luggage)

backpack = luggage["backpack"]       #  luggage["backpack"].sort()
backpack.sort()
print(luggage)

backpack.remove("sandwich")
print(luggage)

luggage["pocket"] += 10
luggage["pocket"] = [50, 10]
print(luggage)



""" Exercise 3
Create a list of dictionary items, where each dictionary represents a book with
keys like "title", "author", and "year". Print the details of all books.
Example output:
Title: The Hitchhiker's Guide to the Galaxy. By Douglas Adams. Published in 1979.
Title: The Great Gatsby. By F. Scott Fitzgerald. Published in 1925.

 """

# solution 

list_of_dicts = [
    {"title": "Oily", "author": "Oluchi", "year": "2025"},
    {"title": "Caregiver", "author": "Prisca", "year": "2026"}
]

for item in list_of_dicts:
    print(f"{item["title"]} by {item["author"]} published in {item["year"]}")





""" Write a program that keeps track of words entered by the user. Create a
dictionary where the keys are words, and the values are the number of times
each word has been entered. Print the dictionary when the user decides to stop
entering words by typing "exit".

Example output:
Please enter a word: hello
Please enter a word: world
Please enter a word: hello
Please enter a word: exit
Summary:
hello: 2
world: 1 """



words = {}
while True:
    word = input("Please enter a word or exit: ")
    if word == "exit":
        break

    if not word in words:
        words[word] = 1
    else:
        words[word] += 1

print(words)
    
