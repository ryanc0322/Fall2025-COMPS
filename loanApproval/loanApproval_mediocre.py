# Author: Woohyeok Choi 2026'
# Mediocre Loan Approval System
# This example is better but still can has major flaws.
# It considers only yes/no factors without nuance which does not 
# consider ranges which is inaccurate.

print("Loan Approval System - Mediocre")

# array that will contain the applicant's score
score = [0,0,0,0,0]
idx = 0

# Name input
while True:
    name = input("What is your name? ").strip()
    if name == "":
        print("Give a valid name.")
    else:
        break

# Employment status
while True:
    employed = input("Are you employed? (yes/no): ").strip().lower()
    if employed != "yes" and employed != "no":
        print("Please enter 'yes' or 'no'.")
    else:
        break

if employed == 'yes':
    score[idx] = 1
idx += 1

# Job stability
while True:
    stable_job = input("Do you have a stable job? \n'yes' if you are paid by salary. (yes/no): ").strip().lower()
    if stable_job != "yes" and stable_job != "no":
        print("Please enter 'yes' or 'no'.")
    else:
        break

if stable_job == 'yes':
    score[idx] = 1
idx += 1

# Monthly income (yes/no, flawed approach)
while True:
    monthly_income = input("Do you have any monthly income? (yes/no): ").strip().lower()
    if monthly_income != "yes" and monthly_income != "no":
        print("Please enter 'yes' or 'no'.")
    else:
        break

if monthly_income == 'yes':
    score[idx] = 1
idx += 1

# Existing loans / debts
while True:
    has_loans = input("Do you have existing loans or debts? (yes/no): ").strip().lower()
    if has_loans != "yes" and has_loans != "no":
        print("Please enter 'yes' or 'no'.")
    else:
        break

if has_loans == 'yes':
    score[idx] = -1
idx += 1

# Assets
while True:
    has_assets = input("Do you own any assets (house, property, etc.)? (yes/no): ").strip().lower()
    if has_assets != "yes" and has_assets != "no":
        print("Please enter 'yes' or 'no'.")
    else:
        break

if has_assets == 'yes':
    score[idx] = 1

score_sum = 0
for i in range(len(score)):
    score_sum += score[i]
    
if score_sum >= 3:
    print("Loan Approved")
else:
    print("Loan Denied")

'''
if employed == "yes" and stable_job == "yes" and monthly_income == "yes" and has_loans == "no":
    print("Loan Approved - stable job, income, and no debts.")
elif has_assets == "yes" and has_income == "yes":
    print("Loan Approved - assets and some income.")
else:
    print("Loan Denied - This system oversimplifies real financial evaluation.")
'''
