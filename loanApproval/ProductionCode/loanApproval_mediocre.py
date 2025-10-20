# Author: Woohyeok Choi 2026'
# Mediocre Loan Approval System
# This example is better but still can has major flaws.
# It considers only yes/no factors without nuance which does not 
# consider ranges which is inaccurate.

# array that will contain the applicant's score 
# you should treat the score array to contain user information in the following format:
# [employment status, job stability, monthly income, existing loans, existing assets]

# Example: Employment status
# This will ask the user if the user is employed or not. 
# We will accept either 'yes' or 'no' from user response. 
def get_employment(employed) :
# we update our score array by changing the first index to '1' if the user is employed
    if employed == 'yes':
        return 1
    return 0


def user_input_employment() :
    while True:
        employed = input("Are you employed? (yes/no): ").strip().lower()
        if employed != "yes" and employed != "no":
            print("Please enter 'yes' or 'no'.")
        else:
            break
    return get_employment(employed)

# Problem 1 - Job stability
# Your task is to implement the user input for whether they have stable job of not. 
# You code should:
# (1) have a clear binary (yes/no) option to accept as user input
# (2) while loop to prevent the program from continuing without a valid input
# (3) clear error message
# (4) update (if the user input is 'yes') the score array at the correct index
def get_job_stability(stable_job) :
    if stable_job == 'yes':
        return 1
    return 0

def user_input_job_stability() :
    while True:
        stable_job = input("Do you have a stable job? \n'yes' if you are paid by salary. (yes/no): ").strip().lower()
        if stable_job != "yes" and stable_job != "no":
            print("Please enter 'yes' or 'no'.")
        else:
            break
    return get_job_stability(stable_job)

# Problem 2 - Monthly income
# Your task is to implement the user input for whether they have a monthly income or not
# You code should:
# (1) have a clear binary (yes/no) option to accept as user input
# (2) while loop to prevent the program from continuing without a valid input
# (3) clear error message
# (4) update (if the user input is 'yes') the score array at the correct index
# (5) Write a short (2-3 sentence) reflection on how a binary answer might be inappropriate 
#     in this context of trying to know user's monthly income for loan approval
def get_monthly_income(monthly_income) :
    if monthly_income == 'yes':
        return 1
    return 0

def user_input_income() :
    while True:
        monthly_income = input("Do you have any monthly income? (yes/no): ").strip().lower()
        if monthly_income != "yes" and monthly_income != "no":
            print("Please enter 'yes' or 'no'.")
        else:
            break
    return get_monthly_income(monthly_income)

# Problem 3 - Existing Loans / Debts
# Your task is to implement the user input for whether they have existing loans or debts
# You code should:
# (1) have a clear binary (yes/no) option to accept as user input
# (2) while loop to prevent the program from continuing without a valid input
# (3) clear error message
# (4) update (if the user input is 'yes') the score array at the correct index
#   * Think about the nature of having 'debt' as opposed to 'income' or 'employment'. 
#   * To what number should the 'loan/debt' index of score array be updated to? 
#   * Hint: employment, monthly income would be a positive factor, whereas loan/debt would be 'negative factor'
# (5) Write a short (2-3 sentence) reflection on how a binary answer might be inappropriate 
#     in this context of trying to know user's existing debt/loan for loan approval
def get_existing_loans(loans) :
    if loans == 'yes':
        return -1
    return 0

def user_input_debt() :
    while True:
        has_loans = input("Do you have existing loans or debts? (yes/no): ").strip().lower()
        if has_loans != "yes" and has_loans != "no":
            print("Please enter 'yes' or 'no'.")
        else:
            break
    return get_existing_loans(has_loans)

# Problem 4 - Assets
# Your task is to implement the user input for whether they have any assets that can be used as mortgage
# You code should:
# (1) have a clear binary (yes/no) option to accept as user input
# (2) while loop to prevent the program from continuing without a valid input
# (3) clear error message
# (4) update (if the user input is 'yes') the score array at the correct index
# (5) Write a short (2-3 sentence) reflection on how a binary answer might be inappropriate 
#     in this context of trying to know user's existing assets for loan approval
def get_assets(assets) :
    if assets == 'yes':
        return 1
    return 0

def user_input_assets() :
    while True:
        has_assets = input("Do you own any assets (house, property, etc.)? (yes/no): ").strip().lower()
        if has_assets != "yes" and has_assets != "no":
            print("Please enter 'yes' or 'no'.")
        else:
            break
    return get_assets(has_asset)

# Problem 5 - Loan Approval / Denial
# 'score_sum' is a variable that will tally up the binary response received from the user so far
# Use a for loop to iterate through the score array and update the score_sum at each iteration
# if 'score_sum' is greater than or equal to 3, then the loan is approved. Else, denied.
def approval(score) :
    score_sum = 0
    for i in range(len(score)):
        score_sum += score[i]
    
    if score_sum >= 3:
        return "Loan Approved"
    else:
        return "Loan Denied"

def main() :
    print("Loan Approval System - Mediocre")
    score = []
    score.append(user_input_employment())
    score.append(user_input_job_stability())
    score.append(user_input_income())
    score.append(user_input_debt())
    score.append(user_input_assets())
    print(approval(score))

if __name__=='__main__':
    main()