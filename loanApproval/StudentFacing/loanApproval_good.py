'''
Good Example of Loan Approval System (Points-Based)
Author: Woohyeok Choi 2026'
This version uses a points-based system to consider multiple factors:
(1) Job stability (salary adds points)
(2) Monthly income (adds points based on thresholds)
(3) Existing loans/debts (subtracts points)
(4) Potential mortgage/property value (adds points)
This is still a simplified teaching model, not a real financial algorithm.
'''

'''
Example: Salary
while loop is used to prevent the program from continuing until a valid input has been inputted from the user
conditionals should be used to check the validity of user input
'''
def get_salary(salary) :
# Based on the salary inputted, points will be added to the corresponding index of the score array 
    if salary >= 5000:
        return 40
    elif salary >= 3000:
        return 25
    elif salary >= 1500:
        return 10


def user_input_salary() :
    while True:
        try:
            salary = int(input("Enter your monthly salary in USD: "))
            if salary <= 0:
                print("Salary should be greater than zero.")
            else:
                break
        except:
            print("Enter a valid salary number.")
        
    return get_salary(salary)

'''
Problem 1 - Monthly income
Your task is to receive user input for any additional monthly income 
(1) If income is greater than or equal to $7000, give 40 points, if income is greater than or equal to
    $4000 give 25 points, and if income is greater than or equal to $2000 give 10 points
(2) update the score array following the point system described above
'''
def get_monthly_income(income) :
      ##PUT YOUR CODE HERE##
      return 

def user_input_income() :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 2 - Loans / Debts
Your task is to receive user input for any loans or debts they have 
(1) If debt is greater than or equal to $50000, give -40 points, if debt is greater than or equal to
    $30000 give -25 points, and if debt is greater than or equal to $10000 give -10 points
(2) update the score array following the point system described above
'''
def get_existing_loans(debts) :
        ##PUT YOUR CODE HERE##
        return 

def user_input_debt() :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 3 - Mortgage / Assets
Your task is to receive user input for any mortgage or assets they have 
(1) If asset value is greater than or equal to $100000, give 30 points, if asset value is greater than or equal to
    $50000 give 15 points, and if asset value is greater than or equal to $20000 give 5 points
(2) update the score array following the point system described above
'''
def get_assets(mortgage) :
        ##PUT YOUR CODE HERE##
        return 

def user_input_assets() :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 4 - Sum
Use for loop to iterate through the score array to calculate the cumulative
sum for the points in the score array
'''
def approval(score) :
    points_sum = 0
    for i in score:
        points_sum += i
    
'''
Problem 5 - Decision
If the final score is greater or equal to 70 then approve loan,
if final score is greater or equal to 40 then "Loan Under Review"
otherwise, loan denied.
'''
    print(f"Your total score is: {points_sum}")

    #Put your condition here
        return "Loan Approved - Strong financial profile."
    #Put your condition here
        return "Loan Under Review - Moderate profile, may need more information."
    #Put your condition here
        return "Loan Denied - Insufficient financial stability."

def main() :
    print("Loan Approval System - Points Based Example")
    score = []
    score.append(user_input_salary())
    score.append(user_input_income())
    score.append(user_input_debt())
    score.append(user_input_assets())
    #Put your print statement here

if __name__=='__main__':
    main()
