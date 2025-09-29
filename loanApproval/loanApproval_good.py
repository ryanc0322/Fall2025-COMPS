# Good Example of Loan Approval System (Points-Based)
# Author: Woohyeok Choi 2026'
# This version uses a points-based system to consider multiple factors:
#  (1) Job stability (salary adds points)
#  (2) Monthly income (adds points based on thresholds)
#  (3) Existing loans/debts (subtracts points)
#  (4) Potential mortgage/property value (adds points)
# This is still a simplified teaching model, not a real financial algorithm.

print("Loan Approval System - Points Based Example")

# Scoring System
points = 0
score = [0,0,0,0,0]
idx = 0

# Name input
while True:
    name = input("What is  your name? ").strip()
    if name == "":
        print("Give a valid name.")
    else:
        break

# Job stability: salary
while True:
    try:
        salary = int(input("Enter your monthly salary in USD: "))
        if salary <= 0:
            print("Salary should be greater than zero.")
        else:
            break
    except:
        print("Enter a valid salary number.")

if salary >= 5000:
    points += 40
elif salary >= 3000:
    points += 25
elif salary >= 1500:
    points += 10
else:
    points += 0

score[idx] = points
idx += 1

# Monthly income
while True:
    try:
        income = int(input("Enter your any additional monthly income in USD: "))
        if income <= 0:
            print("Income must be greater than zero.")
        else:
            break
    except:
        print("Enter a valid income number.")

if income >= 7000:
    points += 40
elif income >= 4000:
    points += 25
elif income >= 2000:
    points += 10
else:
    points += 0

score[idx] = points
idx += 1

# Existing loans / debts
while True:
    try:
        debts = int(input("Enter your any and all existing debts in USD: "))
        if debts < 0:
            print("Debts cannot be negative.")
        else:
            break
    except:
        print("Enter a valid debt number.")

if debts >= 50000:
    points -= 40
elif debts >= 30000:
    points -= 25
elif debts >= 10000:
    points -= 10
else:
    points += 0

score[idx] = points
idx += 1

# Potential mortgage / assets
while True:
    try:
        mortgage = int(input("Enter the estimated value of your property/mortgage in USD: "))
        if mortgage < 0:
            print("Mortgage value cannot be negative.")
        else:
            break
    except:
        print("Enter a valid number for property/mortgage.")

if mortgage >= 100000:
    points += 30
elif mortgage >= 50000:
    points += 15
elif mortgage >= 20000:
    points += 5
else:
    points += 0

score[idx] = points

points_sum = 0
for i in score:
    points_sum += i

# Decision
print(f"Hi {name}, your total score is: {points}")

if points_sum >= 70:
    print("Loan Approved - Strong financial profile.")
elif points_sum >= 40:
    print("Loan Under Review - Moderate profile, may need more information.")
else:
    print("Loan Denied - Insufficient financial stability.")
