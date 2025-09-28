# Basic code for to teach a simple loan approval system using conditionals and loops
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Basic")

while True:
    name = input("Enter your name: ")
    if name == "":
        print("Enter a valid name.")
    else:
        break


while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Enter an age greater than zero.")
        else:
            break
    except:
        print("Enter a valid age")


while True:
    try:
        income = int(input("Enter your monthly income: "))
        if income <= 0:
            print("Income must be a positive number.")
        else:
            break
    except:
        print("Enter a valid income.")


while True:
    try:
        prev_loan = int(input("Enter any existing loans: "))
        if prev_loan < 0:
            print("There cannot be negative loans.")
        else:
            break
    except:
        print("Enter a valid amount for any existing loans.")


while True:
    try:
        desired_loan = int(input("Enter desired loan amount: "))
        if desired_loan <= 0:
            print("There cannot be negative loans.")
        else:
            break
    except:
        print("Enter a valid amount of desired loan requested.")

if age >= 21 and prev_loan <= income * 10  and desired_loan <= income * 10:
    print("Loan Approved")
else:
    print("Loan Denied")


