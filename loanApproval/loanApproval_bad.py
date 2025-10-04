# Extreme example of a loan approval system that is ineffective and unethical
# It shows how focusing on irrelevant or discriminatory criteria
# can create unfair and unethical systems.
# Author: Woohyeok Choi 2026'

print("Loan Approval System - Bad Example")

# Name input
# The while loop prevents the program to continue until it has received a valid input
while True:
    # You should consider the type of input received. In this case 'name' would be string.
    name = input("What is your name? \n>")
    # Check if the user have entered a valid input
    # name cannot be an empty string and must be alphabetical
    if name == "" or not name.isalpha():
        print("Enter a valid name.")
    else:
        break

# Age input
while True:
    # You should consider the type of input received. In this case 'age' should be an int
    # Since any variables received using the input() function is string by default, 
    age = input("What is your age? \n>")
    # Check if the user have entered a valid input
    # age must be a digit
    if not age.isdigit():
        print("Enter a valid age.")
    else:
        # you must use the int() function to convert the input to an int type
        age = int(age)
        break

# Problem 1
# Employment input - Ask if the applicant is employed or not. Your code should:
# (1) prevent the program from continuing without a valid input by using 'while loop'
# (2) give clear instructions on the input() for the user
# (3) consider the input type and convert to the appropriate type if necessary
# (4) give clear error message to instruct the user
# (5) at the end of implementation, reflect and write a short paragraph to why it is unethical to  
#     simply ask whether the person is employed or not without following up with additional questions
#     such as "how much money do you make?"
while True:
    employed = input("Are you employed? (yes/no)\n>")
    if employed not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
    else:
        break


# Problem 2
# Ask for the applicant's contact number and home address. Your code should:
# (1) prevent the program from continuing without a valid input by using 'while loop'
# (2) give clear instructions on the input() for the user
# (3) Home address should be constituted of alphabets and numbers. a function for this is isalnum().
# (4) Phone number should be a positive number. First check if the number is a number, then check if it is positive.
# (5) give clear error message to instruct the user
while True:
    addr = input("What is your home address? \n>")
    if not addr.replace(" ", "").isalnum():  
        print("Please give a valid home address.")
        continue
    break

while True:
    contact = input("Enter your phone number. \n>")
    if not contact.isdigit():
        print("Please give a valid phone number.")
        continue

    contact = int(contact)  

    if contact <= 0:
        print("Phone number should not contain negative number.")
    else:
        break

# Problem 3 
# contacts and address of the 3 people to "refer" to if the applicant fails to pay the loan
# your code should: 
# (1) prevent the program from continuing without a valid input by using 'while loop'
# (2) give clear instructions on the input() for the user
# (3) consider the input type.
# (4) give clear error message to instruct the user
# (5) create two arrays - one for phone numbers and the other for home addresses. 
# (6) use a for loop to iterate three times (for 3 people), ask appropriate questions,
#     and store the phone number and home address into corresponding indicies. 
#     e.g. phone number array = [person 1 phone number, person 2 phone number, person 3 phone number]
#          home addr array = [person 1 home address, person 2 home address, person 3 home address]
phone = [0,0,0]
home = ['a','b','c']

for i in range(3):
    while True:
        phone_contact = input(f"Give the phone number for reference person {i+1} \n>")
        if phone_contact == "" or not phone_contact.isdigit():
            print("Please enter valid a phone number.")
        else:
            phone[i] = phone_contact
            break

    while True:
        home_addr = input(f"Give the home address for reference person {i+1} \n>")
        if home_addr == "" or not home_addr.replace(" ", "").isalnum():
            print("Please enter a valid home address.")
        else:
            home[i] = home_addr
            break

# Problem 4:
# ask a set of questions asking for consent that "traps" the applicant into big liability
# without due consideration of whether the applicants are capable of to the amount of such liability
# your code should:
# (1) create an array to hold the answers of the applicants (yes/no) for each indicies
# (2) create an array to hold onto the questions that will be asked to the applicants
# (3) iterate through a for loop to ask the questions to the applicants and record the answers
questions = [
        "Do you understand that the interest rate (for however amount of money that is borrowed) begins at 20% and increments by 10% every two days?",
        "Do you consent to us treating the three reference people as equally responsible to pay off your debts?",
        "Do you consent to giving up your basic human rights upon your failure to repay your debt?"]

answers = ["","",""]

for i in range(3):
    while True: 
        answer = input(f"{questions[i]} \n>")
        if answer not in ["yes", "no"]:
            print("Please answer in 'yes' or 'no'.")
        else:
            answers[i] = answer
            break

# Problem 5
# Loan approval stage
# Below are example cases that would approve loans
# any other case that does not fit the 'if' or 'elif' clause will be denied loan by falling
# into the 'else' clause
# Your task is to utilize the data inputted from user so far and:
# (1) add two new clauses that would approve the loan 
# (2) add two new clauses that would deny the loan
for i in range(3):
    if answers[i] == "no":
        print("Loan Denied, Sorry.")
        exit()

if employed == "yes":
    print("Loan Accepted. Congrats.")
else:
    print("Loan Denied, Sorry.")
