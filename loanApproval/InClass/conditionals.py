# =============================
# Concept 1: If, Elif, Else
# =============================
# Example 1: Simple condition
temperature = 32
if temperature > 30:
    print("It's hot today!")

# Example 2: If-else
age = 16
if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote.")

# Example 3: If-Elif-Else chain
score = 99
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Activity 1:
# Write a code that checks if a number is positive, negative, or zero.

# Activity 2:
# Ask the user for their age and print whether they’re a child, teen, or adult.

# Activity 3:
# Ask for today’s temperature and print whether it’s “cold,” “warm,” or “hot.”



# ======================================================
# Concept 2: Comparison, Logical Operators, and Nesting
# ======================================================
# Example 1: AND conditions
age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("You can enter the concert!")
else:
    print("Entry not allowed.")

# Example 2: OR condition
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

# Example 3: Nested conditions
score = 92
if score >= 90:
    if score == 100:
        print("Perfect score")
    else:
        print("Great job")
else:
    print("Work harder...")


# Activity 1:
# Ask the user for a number. Print whether it’s even and greater than 10.

# Activity 2:
# Write a simple code that checks whether today is Monday or Friday.

# Challenge: 
# Write a code that checks if a number is divisible by both 3 and 5




# ============================================
# Concept 3: Practicing Conditionals and Looops
# ============================================
# Example 1: Using conditionals inside a loop
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# Example 2: Counting how many numbers are positive
numbers = [3, -1, 0, 5, -7, 2]
positive_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
print(f"Positive number count: {positive_count}")

# Example 3: Simple password attempt system
correct_password = "secretpassword1212"
attempts = 3
while attempts > 0:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Wrong password. {attempts} attempts left.")
if attempts == 0:
    print("Access denied. Try again later.")


# Activity 1:
# Write a loop that counts forever but stops if the user types "stop".

# Activity 2:
# Print numbers 1–10, but skip multiples of 3.

# Activity 3:
# Create a loop that asks for names and stops when the user types "done".

# Challenge:
# Write a loop that counts to 100 but only prints numbers divisible by 5.
