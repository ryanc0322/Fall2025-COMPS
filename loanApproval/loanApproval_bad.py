# Extreme example of a loan approval system that is ineffective and unethical
# It shows how focusing on irrelevant or discriminatory criteria
# can create unfair and unethical systems.
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Bad Example")

# Name input
while True:
    name = input("What is your name? ")
    if name == "":
        print("Enter a valid name.")
    else:
        break

# Gender input
while True:
    gender = input("What is your gender? 'M' for male and 'F' for female ").strip().upper()
    if gender not in ["M", "F"]:
        print("Please enter 'M' or 'F'.")
    else:
        break

# Height input
while True:
    try:
        height = int(input("How tall are you? Answer in cm. "))
        if height <= 0:
            print("Height must be a positive number.")
        else:
            break
    except:
        print("Enter a valid height in numerical value.")

# Favorite color input
while True:
    favorite_color = input("What is your favorite color? ").strip()
    if favorite_color == "":
        print("Please enter a valid color.")
    else:
        break

if gender == "M" and height > 175:
    print("Loan Approved")
elif gender == "F" and favorite_color.lower() == "pink":
    print("Loan Approved")
elif favorite_color.lower() in ["red", "blue"]:
    print("Loan Approved")
else:
    print("Loan Denied")
