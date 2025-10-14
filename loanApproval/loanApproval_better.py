# Better Example of Loan Approval System
# This example improves by using ranges (spectrums) instead of yes/no.
# Author: Woohyeok Choi 2026'

# Below are arrays that will be used to store user data
# 'income' array will store income generated from 'primary job', 'side job', and 'investments'
# 'debt array will store debt from 'credit card', 'car loan' and 'student loan'
# asset will store debt from 'residential propety', 'land ownership', and 'commencial property'
# each type of user input data should be stored in the corresponding  index of the array type
income = [0,0,0]
debt = [0,0,0]
asset = [0,0,0]

# Job stability: monthly salary range
def get_job_stability() :
    has_income = input("Do you have any sources of income? (yes/no): ").strip().lower()
    if has_income == "yes":
        # 1. Generate an array describing the three income type
        # 2. use for-loop to receive user input for each of the three income type
        income_sources = ["primary job salary", "freelance/side income", "investment income"]
        for i, source in enumerate(income_sources):
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

            income[i] = value


# Problem 1 -  Monthly income 
# Write your code to fill up the 'debt' array where the first index should represent 'credit card debt', 
# second index should represent 'car loan debt', and third index should represent 'student loan debt'
# Refer to the example shown above (job stablility). Your code should:
# (1) ask if the user has any debt
# (2) create an array with ["credit card debt", "car loan debt", "student loan debt"]
# (3) use for loop to iterate through the 3 types of debts and receive user input for each type
# (4) have while loop that prevents the user from proceeding without valid input
# (5) check the input is valid (it must be a positive integer) and convert variable type to int
def get_monthly_income() :
    has_debt = input("Do you have any debts? (yes/no): ").strip().lower()
    if has_debt == "yes":
        debt_sources = ["credit card debt", "car loan debt", "student loan debt"]
        for i, source in enumerate(debt_sources):
            while True:
                value = input(f"Enter your cost of debt for {source} (USD): ")
                if not value.isdigit():
                    print("Enter a valid input in numerical value.")
                    continue

                value = int(value)

                if value < 0:
                    print("Enter a positive numerical value")
                else:
                    break

            income[i] = value



# Problem 2 -  Assets 
# Write your code to fill up the 'asset' array where the first index should represent 'residential property', 
# second index should represent 'land ownership', and third index should represent 'commercial property'
# Refer to the example shown above (job stablility). Your code should:
# (1) ask if the user has any asset
# (2) create an array with ["residential property", "land owndership", "commercial property"]
# (3) use for loop to iterate through the 3 types of assets and receive user input for each type
# (4) have while loop that prevents the user from proceeding without valid input
# (5) check the input is valid (it must be a positive integer) and convert variable type to int
def get_assets() :
    has_asset = input("Do you own any assets (property, land, etc.)? (yes/no): ").strip().lower()
    if has_asset == "yes":
        asset_sources = ["residential property", "land ownership", "commercial property"]
        for i, source in enumerate(asset_sources):
            while True:
                value = input(f"Enter the value for your {source} (USD): ")
                if not value.isdigit():
                    print("Enter a valid input in numerical value.")
                    continue

                value = int(value)

                if value < 0:
                    print("Enter a positive numerical value")
                else:
                    break

            income[i] = value

def approval() :
    get_job_stability()
    get_monthly_income()
    get_assets()
# Below are variables that will store the sum of each data type
    income_sum = 0
    debt_sum = 0
    asset_sum = 0

# Problem 3 - Sum
# Use for loop to iterate through each of the three arrays storing user data
# store the resulting sum in the corresponding sum variable created above
    for i in income:
        income_sum += i

    for i in debt:
        debt_sum += i

    for i in asset:
        asset_sum += i

# Simplified approval logic using ranges
# Problem 4 - Conditionals to grant loans
# There are some coditionals that already delineate the type of criteria to give out or deny loans
# (1) Add two more conditions to approve loans and two more conditions to deny loans
# (2) Each conditions should include two or more operatives
    if income_sum >= 3000 and debt_sum <= 20000 and asset_sum >= 50000:
        print("Loan Approved - Strong salary, income, acceptable debts, and property value.")
    elif income_sum >= 2000 and debt_sum <= 30000:
        print("Loan Approved - Moderate salary/income, debts acceptable.")
    elif income_sum < 2000 or debt_sum > 50000:
        print("Loan Denied - Insufficient income or too much debt.")
    else:
        print("Loan Denied - Does not meet the loan criteria.")

def main() :
    print("Loan Approval System - Considers Range")
    approval()

if __name__=='__main__':
    main()
