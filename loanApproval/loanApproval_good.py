# Good Example of Loan Approval System (Points-Based)
# Author: Woohyeok Choi 2026'
# This version uses a points-based system to consider multiple factors:
#  (1) Job stability (salary adds points)
#  (2) Monthly income (adds points based on thresholds)
#  (3) Existing loans/debts (subtracts points)
#  (4) Potential mortgage/property value (adds points)
# This is still a simplified teaching model, not a real financial algorithm.

# Below are variables that will store user's data and scores
# score will hold on to the cumulative point for each category
# idx will point at an index in the score array
score = [0,0,0,0]

# Example: Salary
# while loop is used to prevent the program from continuing until a valid input has been inputted from the user
# conditionals should be used to check the validity of user input
def get_salary() :
    while True:
        try:
            salary = int(input("Enter your monthly salary in USD: "))
            if salary <= 0:
                print("Salary should be greater than zero.")
            else:
                break
        except:
            print("Enter a valid salary number.")

# Based on the salary inputted, points will be added to the corresponding index of the score array 
    if salary >= 5000:
        score[0] = 40
    elif salary >= 3000:
        score[0] = 25
    elif salary >= 1500:
        score[0] = 10

# Problem 2 - Monthly income
# Your task is to receive user input for any additional monthly income 
# (1) If income is greater than or equal to $7000, give 40 points, if income is greater than or equal to
#     $4000 give 25 points, and if income is greater than or equal to $2000 give 10 points
# (2) update the score array following the point system described above
def get_monthly_income() :
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
        score[1] = 40
    elif income >= 4000:
        score[1] = 25
    elif income >= 2000:
        score[1] = 10

# Problem 2 - Loans / Debts
# Your task is to receive user input for any loans or debts they have 
# (1) If debt is greater than or equal to $50000, give -40 points, if debt is greater than or equal to
#     $30000 give -25 points, and if debt is greater than or equal to $10000 give -10 points
# (2) update the score array following the point system described above
def get_existing_loans() :
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
        score[2] = -40
    elif debts >= 30000:
        score[2] = -25
    elif debts >= 10000:
        score[2] = -10


# Problem 3 - Mortgage / Assets
# Your task is to receive user input for any mortgage or assets they have 
# (1) If asset value is greater than or equal to $100000, give 30 points, if asset value is greater than or equal to
#     $50000 give 15 points, and if asset value is greater than or equal to $20000 give 5 points
# (2) update the score array following the point system described above
def get_assets() :
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
        score[3] = 30
    elif mortgage >= 50000:
        score[3] = 15
    elif mortgage >= 20000:
        score[3] = 5


# Problem 4 - Sum
# Use for loop to iterate through the score array to calculate the cumulative
# sum for the points in the score array
def approval() :
    get_salary()
    get_monthly_income()
    get_existing_loans()
    get_assets()

    points_sum = 0
    for i in score:
        points_sum += i

# Problem 5 - Decision
# If the final score is greater or equal to 70 then approve loan,
# if final score is greater or equal to 40 then "Loan Under Review"
# otherwise, loan denied.
    print(f"Your total score is: {points_sum}")

    if points_sum >= 70:
        print("Loan Approved - Strong financial profile.")
    elif points_sum >= 40:
        print("Loan Under Review - Moderate profile, may need more information.")
    else:
        print("Loan Denied - Insufficient financial stability.")

def main() :
    print("Loan Approval System - Points Based Example")
    approval()

if __name__=='__main__':
    main()