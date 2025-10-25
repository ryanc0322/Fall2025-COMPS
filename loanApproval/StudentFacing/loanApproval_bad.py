'''
Extreme example of a loan approval system that is ineffective and unethical
It shows how focusing on irrelevant or discriminatory criteria
can create unfair and unethical systems.
Author: Woohyeok Choi 2026'
'''

'''
EXAMPLE FUNCTIONS:
Name input function
The while loop prevents the program to continue until it has received a valid input.
'''
def get_name() :
    while True:
        # You should consider the type of input received. In this case 'name' would be string.
        name = input("What is your name? \n>")
        # Check if the user have entered a valid input
        # name cannot be an empty string and must be alphabetical
        if name == "" or not name.isalpha():
            print("Enter a valid name.")
        else:
            break
    return name
  
'''    
Age input function
Employs same strategy as function above.
'''
def get_age() :
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
    return age

'''
Gender input function
'''
def get_gender() :
    while True:
        gender = input("What is your gender? 'M' or 'F'\n>")
        if gender not in ["M", "F"]:
            print("Enter a valid gender.")
        else:
            break
    return gender

'''
Problem 1
Employment input - Ask if the applicant is employed or not. Your code should:
(1) prevent the program from continuing without a valid input by using 'while loop'
(2) give clear instructions on the input() for the user
(3) consider the input type and convert to the appropriate type if necessary
(4) give clear error message to instruct the user
(5) return the input answer
(6) at the end of implementation, reflect and write a short paragraph to why it is unethical to  
    simply ask whether the person is employed or not without following up with additional questions
    such as "how much money do you make?"
'''
def get_employment() :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 2
Ask for the applicant's contact number and home address. Your code should:
(1) prevent the program from continuing without a valid input by using 'while loop'
(2) give clear instructions on the input() for the user
(3) Home address should be constituted of alphabets and numbers. a function for this is isalnum().
(4) Phone number should be a positive number. First check if the number is a number, then check if it is positive.
    Remember that any input is initially a string.
(5) Return the input answers for both functions
(6) give clear error message to instruct the user
'''
def get_address() :
    ##PUT YOUR CODE HERE##
    return

def get_phone() :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 3 
Contacts and address of the 3 people to "refer" to if the applicant fails to pay the loan
your code should: 
(1) prevent the program from continuing without a valid input by using 'while loop'
(2) give clear instructions on the input() for the user
(3) consider the input type.
(4) give clear error message to instruct the user
(5) create two arrays - one for phone numbers and the other for home addresses. 
(6) use a for loop to iterate three times (for 3 people), ask appropriate questions,
    and store the phone number and home address into corresponding indicies. 
    e.g. phone number array = [person 1 phone number, person 2 phone number, person 3 phone number]
         home addr array = [person 1 home address, person 2 home address, person 3 home address]
    Then, return a list of tuples by using the built-in function zip() to bind the two lists together
'''
def get_references() :
    ##PUT YOUR CODE HERE##
    return 

'''
Problem 4:
ask a set of questions asking for consent that "traps" the applicant into big liability
without due consideration of whether the applicants are capable of to the amount of such liability
your code should:
(1) create an array to hold the answers of the applicants (yes/no) for each indicies
(2) create an array to hold onto the questions that will be asked to the applicants
(3) iterate through a for loop to ask the questions to the applicants and record the answers
(4) return the array of answers for the questions
'''
def ask_questions() :
    ##PUT YOUR CODE HERE##
    return

'''
Problem 5
Loan approval stage
Below are example cases that would approve loans
any other case that does not fit the 'if' or 'elif' clause will be denied loan by falling
into the 'else' clause
Your task is to utilize the data inputted from user so far and:
(1) add two new clauses that would approve the loan 
(2) add two new clauses that would deny the loan
'''
def approval(answers, employed, gender) : ##You will need to decide what things a function will need, this is just an example. Feel free to change.
    ##Your condition here
        return "Loan Denied, Sorry."

    if ##Your condition here:
        return "Loan Accepted. Congrats."
    else:
        return "Loan Denied, Sorry."

'''
A main function to help run each of the helper functions.
'''
def main() :
    print("Loan Approval System - Bad Example")
    name = get_name()
    age = get_age()
    gender = get_gender()
    employed = get_employment()
    address = get_address()
    phone = get_phone()
    references = get_references()
    answers = ask_questions()
    ##Put a print statement for approval here

if __name__=='__main__':
    main()
