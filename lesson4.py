""" word = input("enter a word: ")
character = None
count = 0
for character in word:
    if character.lower() == "e":
        count += 1
print(count) 



sentence = input("enter a sentence: ")
for character in sentence:
    print(character)
    



sentence = input("enter a sentence: ")
character =None
count = 0
for character in sentence:
    print(character)
    count += 1
print(f" The sentence has {count} characters.")


sentence = "Hello, Redi!"
counter = 0
for element in sentence:
    print(counter, element)
    counter += 1



Ask the user for a sentwence
print when the index is a multiple of 3

sentence = "Hello, Redi!"
counter = 0
for element in sentence:
    if (counter % 3 == 0):
        print("The index of " + str(element) + " is " + str(counter))
    counter += 3



numbers = [12, 3, 5, 19, 7, 3, 1, 5]
sum = 0
for number in numbers:
    sum += number
print(sum)


 """

names = ["Joy", "Faith", "Oluchi", "Vicky"]
names.append("Prisca")
names.insert(2, "Mine")
print(names)
names[3] = "Oli"
print(names)
names.pop(0)   # or names.remove("Joy")
print(names)
print(len(names))
names.sort()
print(names)