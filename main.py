# Author - Luke Hepokoski
# Description: This program is a random function program that can perform
# multiple functions, ranging from text display to math problems. It will
# utilize more Python functions as I learn them throughout the course.

# Sources used: https://www.hackerrank.com/
# Imports the math module for later functions
import math

# Prints the statement "Hi!"  5 times

print("Hi! " * 5)

# States hello to the user, date of program and requests user name

print("Hello there user! Welcome to my random function program!")
print("This program was created on", end=' ')
print("9", "12", "2021", sep='-')
print("Before proceeding, what is your name?")

# Defines name as a variable for the user to enter their name

name_user = input("Enter your name: ")

# Prints: Hello "user's name"! Welcome to the random function program!"

print("Hello", name_user + "!" "\nWelcome to the random function program!")
print(
    "For this program, you have several options of functions to choose from, "
    "however let's start with an example.")

# Define a whole set of unnecessary variables for the print statement below

animal = input("Enter a name of an animal: ")
color = input("Enter a color: ")
name_vehicle = input("Enter vehicle name: ")
name_city = input("Enter city name: ")
to = " to "
the = "The "
drove = " drove the "

# Print statement utilizing above variables and the + operator to combine
# strings

print(
    the + color + " " + animal + drove + name_vehicle + to + name_city + ".")
print(
    "Ha! See? This program can perform any function it wants to. Now, "
    "input whatever you want and watch it output on the screen!")
statement_user = input("Input text here: ")  # yser input statement for fun
print(statement_user)
print(
    "Congratulations, you've now printed a statement. Now time for the math "
    "problems!",
    "\n" "Enter a number below")

# Sets variable for first number inputted

first_num = (float(
    input()))  # uses float for all below since decimals can accomodate more
# numbers
print(first_num)
print("Great! Now let's try adding that number and another number!")

# Defines a variable for the addition operation and executes it

second_num = (float(input()))
# Adds first input to second input and creates a variable for it
added_num = (
        first_num + second_num)
print(added_num)  # prints variable value
print("Now try subtracting a number from that number!")

# Defines a variable for the subtraction operation and executes it

third_num = (float(input()))
sub_add = (added_num - third_num)
print(sub_add)
print("How about multiplication now?")

# Defines a variable for the multiplication operation and executes it

mult_num = (float(input()))
# Multiplication of subtracted number by user value
mult_add = (
        sub_add * mult_num)
print(mult_add)
print("Division?")

# Defines a variable for the division operation and executes it

fourth_num = (float(input()))
div_add = (mult_add / fourth_num)  # division of previous number by user input
print(div_add)
print("Now let's use exponents!")

# Defines a variable for the exponent operation and executes it

fifth_num = (float(input()))
# Previous number raised to exponent of user value
expo_add = (
        div_add ** fifth_num)
print(expo_add)

# Defines a variable for the floor division operation and executes it

print("Now onto some trickier problems, let's use floor division.")
sixth_num = (float(input()))
# Floor division of previous number and user value
floor_div_add = (
        expo_add // sixth_num)
print(floor_div_add)

# Defines a variable for the modulus operation and executes it

print("Continuing on, let's find a modulus.")
seventh_num = (float(input()))
# Modulus of previous number and inputted number
modulus_add = (
        floor_div_add % seventh_num)
print(modulus_add)

# Creates a print statement and creates the grade variable
# Uses boolean operators to check for user input values between
# Certain numbers and prints the corresponding print statements
print("Now let's check how well you did in your class.")
grade = int(input("Enter your grade: "))
if grade <= 100 and grade >= 90:
    print("You got an A!")
elif grade <= 89 and grade >= 80:
    print("Nice a B.")
elif grade <= 79 and grade >= 70:
    print("C's get degrees.")
elif grade <= 69 and grade >= 60:
    print("D")
elif grade > 100 or grade < 0:
    print("Error")
else:
    print("Fail")

# Program for having a user select an input from 1-5

# Creates variable for while loop

continue_program = True

while continue_program:

    # Prints choices for user to select from
    print("Enter the choice for what you would like to see")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

    # User input
    user_choice = input()

    # Options that happen when the user selects a number
    if user_choice == "1":
        print("You have called function number 1")
    elif user_choice == "2":
        print("You have called function number 2")
    elif user_choice == "3":
        print("You have called function number 3")
    elif user_choice == "4":
        print("You have called function number 4")

    elif user_choice == "5":
        # Ends the loop if the user chooses 5
        continue_program = False
    # If the user selects any other input, prints the error message below
    else:

        print("Invalid selection. Try again.")
# Program for calculating the average grade of 3 users

# Sets total grade to 0 since no grade has been inputted
total = 0

# Creates a for loop that runs one time for a user name and 3 grade input
for name in range(1):
    name = input("Please enter a name. ")
    for score in range(3):
        score = int(input("Please enter a grade. "))
        total = total + score
    # Takes the total and divides it by 3 to find average grade
    avg = total / 3
    total = 0  # Resets the value to 0
    print("Name:", name)
    # Prints the average and formats it to 2 decimals
    print("Average:", format(avg,
                             '.2f'))
# Creates a program to test if the user inputs a number and restarts if no
# number is inputted
program_on = True
# Creates while loop for program
while program_on:
    firstNumber = input("Please enter a whole number: ")
    # Tests to see if user input is an integer or not
    try:
        int(firstNumber)
        print("Valid")
        program_on = False
    # If the input isn't an integer, prints error message and restarts loop
    except ValueError:
        print("That was not a valid number. Please try again.")
# Creates a program to input a letter that is between a-z
print("Input a letter, if it's lowercase it'll print, otherwise it won't.")
letter = input()
while letter >= "A" and letter <= "Z":
    letter = input()
print(letter)


def calculate_area(radius):
    area = math.pi * radius ** 2
    print("The area of the circle given a radius of", radius, "is",
          format(area, ".2f"))


def calculate_diameter(radius):
    area = radius * 2
    print("Diameter of a circle with a radius of", radius, "is",
          format(area, ".2f"))


def calculate():
    radius = int(input(
        "Here we have a program to calculate the area and diameter of a "
        "circle"" given a radius, please enter a radius. "))
    calculate_area(radius)
    calculate_diameter(radius)


calculate()
user_word_input = input(
    "Here we will compare the ASCII values of two different words or "
    "letters, if they are equal it will print True, if not it will print "
    "False." "\n" "Enter a word or letter. ")
user_word_input_2 = input("Enter a second word or letter. ")
if user_word_input != user_word_input_2:
    print("False")
else:
    print("True")

# Uses the not variable to print False since the variable is within the range
x = 5
print(not (3 < x < 10))
