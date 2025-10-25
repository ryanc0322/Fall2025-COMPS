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

##PUT YOUR CODE HERE##
