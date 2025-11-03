'''
Better Example of Loan Approval System
This example improves by using ranges (spectrums) instead of yes/no.
Author: Woohyeok Choi 2026'

Below are arrays that will be used to store user data
'income' array will store income generated from 'primary job', 'side job', and 'investments'
'debt array will store debt from 'credit card', 'car loan' and 'student loan'
asset will store debt from 'residential propety', 'land ownership', and 'commencial property'
each type of user input data should be stored in the corresponding  index of the array type
'''

'''
Job stability: monthly salary range
'''
def get_income() :
    income = []
    has_income = input("Do you have any sources of income? (yes/no): ").strip().lower()
    if has_income == "yes":
        # 1. Generate an array describing the three income type
        # 2. use for-loop to receive user input for each of the three income type
        income_sources = ["primary job salary", "freelance/side income", "investment income"]
        for i, source in enumerate(income_sources):
            income[i] = user_input_income(source)
    else :
        for i in range(3) :
            income.append(0)
    return income

def user_input_income(source) :
# 3. use while loop to prevent program from continuing until valid input has been accepted
    while True:
        value = input(f"Enter your monthly {source} (USD): ")
        if not value.isdigit():
            print("Enter a valid input in numerical value.")
            continue

        value = int(value)

        if value < 0:
            print("Enter a positive numerical value")
        else:
            break
        
        return value

'''
Problem 1 -  Debts
Write your code to fill up the 'debt' array where the first index should represent 'credit card debt', 
second index should represent 'car loan debt', and third index should represent 'student loan debt'
Refer to the example shown above (job stablility). Your code should:
(1) ask if the user has any debt
(2) create an array with ["credit card debt", "car loan debt", "student loan debt"]
(3) use for loop to iterate through the 3 types of debts and receive user input for each type
(4) have while loop that prevents the user from proceeding without valid input
(5) check the input is valid (it must be a positive integer) and convert variable type to int
'''
def get_debt() :
  ##PUT YOUR CODE HERE##
    return 

def user_input_debt(source) :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 2 -  Assets 
Write your code to fill up the 'asset' array where the first index should represent 'residential property', 
second index should represent 'land ownership', and third index should represent 'commercial property'
Refer to the example shown above (job stablility). Your code should:
(1) ask if the user has any asset
(2) create an array with ["residential property", "land owndership", "commercial property"]
(3) use for loop to iterate through the 3 types of assets and receive user input for each type
(4) have while loop that prevents the user from proceeding without valid input
(5) check the input is valid (it must be a positive integer) and convert variable type to int
'''
def get_assets() :
    ##PUT YOUR CODE HERE##
    return 

def user_input_assets(source) :
    ##PUT YOUR CODE HERE##
    return 

def approval(income, debt, assets) :
# Below are variables that will store the sum of each data type
    income_sum = 0
    debt_sum = 0
    asset_sum = 0
'''
Problem 3 - Sum
Use for loop to iterate through each of the three arrays storing user data
store the resulting sum in the corresponding sum variable created above
'''   
    ##PUT YOUR CODE HERE##

# Simplified approval logic using ranges
# Problem 4 - Conditionals to grant loans
# There are some coditionals that already delineate the type of criteria to give out or deny loans
# (1) Add two more conditions to approve loans and two more conditions to deny loans
# (2) Each conditions should include two or more operatives
    if income_sum >= 3000 and debt_sum <= 20000 and asset_sum >= 50000:
        return "Loan Approved - Strong salary, income, acceptable debts, and property value."
    elif ##YOUR CONDITION HERE##:
        return "Loan Approved - Moderate salary/income, debts acceptable."
    elif ##YOUR CONDITION HERE:
        return "Loan Denied - Insufficient income or too much debt."
    else:
        return "Loan Denied - Does not meet the loan criteria."

def main() :
    print("Loan Approval System - Considers Range")
    income = get_income()
    debt = get_debt()
    assets = get_assets()
    ##PUT YOUR PRINT STATEMENT HERE##

if __name__=='__main__':
    main()
