# Extreme example of a loan approval system that is ineffective and unethical
# It shows how focusing on irrelevant or discriminatory criteria
# can create unfair and unethical systems.
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Bad Example")

# Name input
# The while loop prevents the program to continue until it has received a valid input
while True:
    # You should consider the type of input received. In this case 'name' would be string.
    name = input("What is your name? \n>")
    # Check if the user have entered a valid input
    # name cannot be an empty string and must be alphabetical
    if name == "" or not name.isalpha():
        print("Enter a valid name.")
    else:
        break

# Age input
while True:
    # You should consider the type of input received. In this case 'age' should be an int
    # Since any variables received using the input() function is string by default, 
    age = input("What is your age? \n>")
    # Check if the user have entered a valid input
    # age must be a digit
    if not age.isdigit():
        print("Enter a valid age.")
    else:
        # you must use the int() function to convert the input to an int type
        age = int(age)
        break

# Problem 1
# Gender input - Receive a gender input from the user your code should:
# (1) prevent the program from continuing without a valid input by using 'while loop'
# (2) give clear instructions on the input() for the user
# (3) consider the input type and convert to the appropriate type if necessary
# (4) give clear error message to instruct the user
while True:
    gender = input("What is your gender? 'M' for male and 'F' for female \n>")
    if gender not in ["M", "F"]:
        print("Please enter 'M' or 'F'.")
    else:
        break


# Problem 2
# Height input - Receive the user's height. Your code should:
# (1) prevent the program from continuing without a valid input by using 'while loop'
# (2) give clear instructions on the input() for the user
# (3) Height should be a positive number. First check if the number is a number, then check if it is positive.
# (4) give clear error message to instruct the user
while True:
    height = input("How tall are you? Answer in cm. \n>")
    if not height.isdigit():  
        print("Enter a valid height in numerical value.")
        continue

    height = int(height)  

    if height <= 0:
        print("Height must be a positive number.")
    else:
        break

# Problem 3 
# Favorite color input
# (1) prevent the program from continuing without a valid input by using 'while loop'
# (2) give clear instructions on the input() for the user
# (3) consider the input type. Color should be a string type
# (4) give clear error message to instruct the user
while True:
    favorite_color = input("What is your favorite color? \n>").strip()
    if favorite_color == "" or not favorite_color.isalpha():
        print("Please enter a valid color.")
    else:
        break


# Problem 4
# Loan approval stage
# Below are example cases that would approve loans
# any other case that does not fit the 'if' or 'elif' clause will be denied loan by falling
# into the 'else' clause
# Your task is to utilize the data inputted from user so far and:
# (1) add three new clauses that would approve the loan 
# (2) add three new clauses that would deny the loan
if gender == "M" and height > 175:
    print("Loan Approved, Congrats.")
elif gender == "F" and favorite_color.lower() == "pink":
    print("Loan Approved, Congrats.")
elif favorite_color.lower() in ["red", "blue"]:
    print("Loan Approved, Congrats.")
else:
    print("Loan Denied, Sorry.")
