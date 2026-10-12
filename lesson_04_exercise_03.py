
"""Exercise 3
Write a program that asks the user for their favorite colors (up to 5)
and stores them in a list. Then, create a sentence that says,
"Your favorite colors are: color1, color2, ..." using the .join() function.
"""


# Exercise 3 solution

while True:
    #Ask the user for input
    colors_input = input("Enter exactly 5 of your favorite colors, separated by commas: ")

    #Split by comma and clean up whitespace, ignoring empty entries
    colors_list = [color.strip() for color in colors_input.split(",") if color.strip()]
    
    #Count how many colors were entered
    color_count = len(colors_list)

    #Check conditions using if-elif-else
    if color_count < 5:
        print(f"You only entered {color_count} colors. Please enter exactly 5.")
        
    elif color_count > 5:
        print(f"You entered {color_count} colors. Please enter exactly 5.")
        
    else:
        break  # Exit the loop successfully

#Join the list and print the final result
colors_string = ", ".join(colors_list)
print(f"Your favorite colors are: {colors_string}")