# ==================================
# Concept 1: Repetition & For Loops 
# ==================================
# Example 1: Counting numbers
for i in range(1, 6):  # start=1, stop=6 (not inclusive)
    print(f"Step {i}")

# Example 2: Printing names from a list
students = ["Alice", "Ben", "Chloe"]
for name in students:
    print(f"Good morning, {name}!")

# Example 3: Summing numbers
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print(f"Total: {total}")


# Reflection:
# For loops help us automate tasks by repeating actions. In real systems (ex: grade books, 
# email systems, job applications), loops might process thousands of people or decisions at once — fast.
# If your loop accidentally skipped someone or processed a name incorrectly, how could that 
# affect them?

# Activities:
# 1) Write a for loop that prints the numbers from 10 to 20.
# 2) Print every fruit from this list: ["apple", "banana", "cherry", "kiwi"].
# 3) Write a loop that sums all numbers from 1 to 100 and then print the sum.
# 4) Challenge: Print only the even numbers from 2 to 100.




# =========================
# Concept 2 — While Loops
# =========================
# Example 1: Countdown
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("KABOOM!")

# Example 2: Guess the number
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess the secret number between 1–10: "))
print("You guessed the secret number!")

# Example 3: Keep reading until condition met
temperature = 20
while temperature < 30:
    print(f"Temperature is {temperature}°C — safe.")
    temperature += 2
print("Temperature too high!")

# Infinite loop (don't run indefinitely)
# while True:
#     print("This will never stop! (unless you press ctrl-c)")

# Reflection:
# While loops continue until a condition changes. In real-world applications (ex: login attempts,
# data processing), an infinite loop could lock someone out of their account or crash a system.
# How can you design while loops to ensure they always reach a stopping point safely while also
# preserving security integrity (not allowing someone an infinite number of password attempts)?

# Activities:
# 1) Write a while loop  counting from 1 to 10.
# 2) Create a password checker that keeps asking for input until the user types "openplease123!".
# 3) Write a program that continuously prints “Loading...” until a variable counts up and reaches 100.
# 4) Challenge: Create a very simple guessing game that allows only 3 chances to guess correctly.




# =========================
# Concept 3 — Nested Loops
# =========================
# Example 1: Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("----")

# Example 2: Seating Charts
rows = ["A", "B", "C"]
for row in rows:
    for seat in range(1, 4):
        print(f"Seat: {row}{seat}")

# Example 3: Grid coordinates
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})", end=" ")
    print()


# Reflection: How could nested loops accidentally create unequal or biased outcomes?
# Think about a real-world situation where a nested for-loop is likely to be used, and another 
# real-world situation where a nested while-loop is likely to be used. For each cases, what
# would be a way to distinguish between the data / item iterating through the loop? When 
# would it be inappropriate to make such distinguishment across the item? 

# Activities:
# 1) Write a nested loop to print a 5×5 grid of stars (*).
# 2) Use nested loops to print combinations of shirts and pants below
shirts = ["red", "blue"]
pants = ["black", "white"]

# 3) Write a nested loop that prints all possible pairs of numbers from 1 to 3 and 4 to 6.
# 4) Challenge: Build a mini multiplication table for numbers 1–5.
