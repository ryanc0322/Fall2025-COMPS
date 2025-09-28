# weighted scoring system that ethically penalizes freelance job
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Stable Income Bias")

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
        income_type = int(input("Are you salaried or freelancer? \n (1) Salaried \n (2) Freelancer \n > "))
        if income_type != 1 and income_type != 2:
            print("Enter a valid input. 1 for salaried and 2 for freelancer")
        else:
            break
    except:
        print("Enter a valid value.")
    

score = income 

if income_type == 1:
    score += 1000

if score >= 2000:
    print("Loan Approved")
else:
    print("Loan Denied")


