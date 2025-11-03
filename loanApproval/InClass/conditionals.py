# ============================================================
# Concept 1: If, Elif, Else — Fairness & Avoiding Bias
# ============================================================
# Example 1: Simple condition (weather service)
temperature = 38
if temperature > 35:
    print("It is very hot today. Make sure to stay hydrated.")

# Example 2: If-else — Fair decision making
# Imagine a voting system that checks eligibility
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You are currently too young to vote")

# Example 3: If-Elif-Else chain — grading without judgment
score = 99
if score >= 90:
    print("Grade: A — Excellent work")
elif score >= 80:
    print("Grade: B — Great job")
elif score >= 70:
    print("Grade: C — Keep practicing")
else:
    print("Grade: F — Please study more")

# Reflection prompt for students:
# How can conditional systems accidentally treat people unfairly?
# (Examples: financial systems, job application filters, age-based services)

# Activities
# 1) Classify numbers as positive/negative/zero respectfully.
# 2) Age categories: child, teen, adult — avoid stereotypes (every stage matters).
# 3) Weather categories: cold, warm, hot — include health/safety advice.


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


# Reflection prompt:
# Systems classify people — in what ways should we use conditionals to not marginalize people?
# (Loan approvals, school placement, job screening — we must design fairly)


# Activities:
# 1) Ask the user for a number. Print whether it’s even and greater than 10.
# 2) Write a simple code that checks whether today is Monday or Friday.
# 3) Challenge: Write a code that checks if a number is divisible by both 3 and 5




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

# Reflection prompt:
# When you design a program that makes decisions (like checking passwords 
# or choosing what to print), how can those decisions affect real people?
# What should you keep in mind to ensure fairness and respect?

# Activities:
# 1) Write a loop that counts forever but stops if the user types "stop".
# 2) Print numbers 1–10, but skip multiples of 3.
# 3) Create a loop that asks for names and stops when the user types "done".
# 4) Challenge: Write a loop that counts to 100 but only prints numbers divisible by 5.
