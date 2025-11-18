# ==============================
# Loops & Conditionals Worksheet
# ==============================

#===================
# Basic Conditionals
#===================
# Question 1
# Write a program that checks if a number entered by the user is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Question 2
# Ask the user for their age, and print:
# • “Child” if below 13
# • “Teenager” if between 13 and 19
# • “Adult” otherwise
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
else:
    print("Adult")


# Question 3
# Write a program that checks whether a given number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question 4
# Ask the user to enter a password.
# If it matches "pass12word34", print “Access granted.” Otherwise, print “Access denied.”
password = input("Enter password: ")
if password == "pass12word34":
    print("Access granted")
else:
    print("Access denied")


# Question 5
# Ask the user for a number.
# If it’s divisible by both 3 and 5, print “FizzBuzz”.
# If only by 3 → “Fizz”.
# If only by 5 → “Buzz”.
# Otherwise print the number.
num = int(input("Input number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)




#===================
# Basic Loops
#===================
# Question 6
# Print all numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)



# Question 7
# Print all even numbers between 1 and 20 using a for loop.
for i in range(2, 21, 2):
    print(i)



# Question 8
# Write a program that prints the multiplication table of 7.
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")



# Question 9
# Use a while loop to count down from 10 to 1, then print “KABOOM"
count = 10
while count > 0:
    print(count)
    count -= 1
print("Lift off!")



# Question 10
# Ask the user to keep entering numbers until they type 0.
# Print the sum of all numbers entered.
total = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))
print(f"Sum: {total}")



#======================
# Loops & Conditionals
#======================
# Question 11
# Print all numbers from 1 to 30, but skip numbers that are multiples of 3.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)


# Question 12
# Ask the user for 5 numbers, and print how many of them are positive.
positive_count = 0
for i in range(5):
    num = int(input("Enter a number: "))
    if num > 0:
        positive_count += 1
print(f"Positive numbers: {positive_count}")


# Question 13
# Ask the user for 10 numbers.
# Count how many are positive, negative, and zero.
pos = neg = zero = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print(f"Positive: {pos}, Negative: {neg}, Zero: {zero}")


# Question 14
# Write a program that prints all prime numbers between 2 and 20.
for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# Question 15
# Ask the user to enter 5 grades.
# Calculate and print the average.
# If average ≥ 90 then “Excellent”, 70–89 then  “Good”, below 70 then “Work harder”.
total = 0
for i in range(5):
    grade = float(input("Enter grade: "))
    total += grade
average = total / 5

if average >= 90:
    print("Excellent")
elif average >= 70:
    print("Good")
else:
    print("Needs improvement")



# Question 16
# Print a triangle of stars like this:
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)


# Question 17
# Ask the user for a number n, and print whether it’s a perfect square.
import math
n = int(input("Enter a number: "))
if math.isqrt(n)**2 == n:
    print("Perfect square")
else:
    print("Not a perfect square")



# ===================
# Challenge Questions
# ===================
# Question 18
# Write a program that prints the following pattern using nested loops and conditionals:
#     1
#    3 5
#   7 9 11
#  13 15 17 19
num = 1
rows = 4
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print odd numbers
    for k in range(i):
        print(num, end=" ")
        num += 2
    print()



# Question 19
# Ask the user to enter 5 words.
# For each word, print how many vowels (a, e, i, o, u) it contains.
# Then print the word with the most vowels.
max_vowels = 0
word_with_max = ""

for i in range(5):
    word = input("Enter a word: ").lower()
    count = 0
    for ch in word:
        if ch in "aeiou":
            count += 1
    print(f"'{word}' has {count} vowels.")

    if count > max_vowels:
        max_vowels = count
        word_with_max = word

print(f"Word with the most vowels is '{word_with_max}' ({max_vowels} vowels).")



# Question 20
# Simulate an ATM where a user starts with a balance of $500.
# Use a while loop to keep showing options until they choose to exit.
balance = 500

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited ${amount}. New balance: ${balance}")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
        else:
            print("Insufficient money")

    elif choice == "3":
        print(f"Current balance: ${balance}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again.")



