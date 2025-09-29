# Better Example of Loan Approval System
# This example improves by using ranges (spectrums) instead of yes/no.
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Considers Range")

income = [0,0,0]
debt = [0,0,0]
asset = [0,0,0]

# Job stability: monthly salary range
has_income = input("Do you have any sources of income? (yes/no): ").strip().lower()
if has_income == "yes":
    income_sources = ["primary job salary", "freelance/side income", "investment income"]
    for i, source in enumerate(income_sources):
        while True:
            try:
                value = int(input(f"Enter your monthly {source} (USD): "))
                if value < 0:
                    print("Value cannot be negative.")
                else:
                    income[i] = value
                    break
            except:
                print("Enter a valid number.")

# Monthly income 
has_debt = input("Do you have any debts? (yes/no): ").strip().lower()
if has_debt == "yes":
    debt_sources = ["credit card debt", "car loan debt", "student loan debt"]
    for i, source in enumerate(debt_sources):
        while True:
            try:
                value = int(input(f"Enter your {source} (USD): "))
                if value < 0:
                    print("Value cannot be negative.")
                else:
                    debt[i] = value
                    break
            except:
                print("Enter a valid number.")

total_debt = sum(debt)
print(f"Total debts recorded: {total_debt}")


# Existing loans / debts
has_asset = input("Do you own any assets (property, land, etc.)? (yes/no): ").strip().lower()
if has_asset == "yes":
    asset_sources = ["residential property value", "land ownership value", "commercial property value"]
    for i, source in enumerate(asset_sources):
        while True:
            try:
                value = int(input(f"Enter your {source} (USD): "))
                if value < 0:
                    print("Value cannot be negative.")
                else:
                    asset[i] = value
                    break
            except:
                print("Enter a valid number.")

total_asset = sum(asset)
print(f"Total assets recorded: {total_asset}")


income_sum = 0
debt_sum = 0
asset_sum = 0

for i in income:
    income_sum += i

for i in debt:
    debt_sum += i

for i in asset:
    asset_sum += i

# Simplified approval logic using ranges
if income_sum >= 3000 and debt_sum <= 20000 and asset_sum >= 50000:
    print("Loan Approved - Strong salary, income, acceptable debts, and property value.")
elif income_sum >= 2000 and debt_sum <= 30000:
    print("Loan Approved - Moderate salary/income, debts acceptable.")
elif income_sum < 2000 or debt_sum > 50000:
    print("Loan Denied - Insufficient income or too much debt.")
else:
    print("Loan Denied - Does not meet the loan criteria.")
