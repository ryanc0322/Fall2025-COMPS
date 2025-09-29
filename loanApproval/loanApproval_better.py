# Better Example of Loan Approval System
# This example improves by using ranges (spectrums) instead of yes/no.
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Considers Range")

# Name input
while True:
    name = input("What is your name? ").strip()
    if name == "":
        print("Give a valid name.")
    else:
        break

# Job stability: monthly salary range
while True:
    try:
        salary = int(input("Enter your monthly salary in USD: "))
        if salary <= 0:
            print("Salary must be greater than zero.")
        else:
            break
    except:
        print("Enter a valid salary number.")

# Monthly income 
while True:
    try:
        income = int(input("Enter any additional monthly income in USD: "))
        if income <= 0:
            print("Income must be greater than zero.")
        else:
            break
    except:
        print("Enter a valid income number.")

# Existing loans / debts
while True:
    try:
        debts = int(input("Enter your total existing debts in USD: "))
        if debts < 0:
            print("Debts cannot be negative.")
        else:
            break
    except:
        print("Enter a valid debt number.")

# Potential mortgage (asset value / property value)
while True:
    try:
        mortgage = int(input("Enter the estimated value of your property/mortgage in USD: "))
        if mortgage < 0:
            print("Mortgage value cannot be negative.")
        else:
            break
    except:
        print("Enter a valid number for property/mortgage.")

# Simplified approval logic using ranges
if salary >= 3000 and income >= 4000 and debts <= 20000 and mortgage >= 50000:
    print("Loan Approved - Strong salary, income, acceptable debts, and property value.")
elif salary >= 2000 and income >= 2500 and debts <= 30000:
    print("Loan Approved - Moderate salary/income, debts acceptable.")
elif income < 2000 or debts > 50000:
    print("Loan Denied - Insufficient income or too much debt.")
else:
    print("Loan Denied - Does not meet the loan criteria.")
