import random

print("Basic Purchase Simulator:")

while True:
    name = input("What is your name? \n>")
    if name == "" or not name.isalpha():
        print("Enter a valid name.")
    else:
        break

while True:
    try:
        balance = int(input("Enter your current balance: "))
        if balance <= 0:
            print("Balance must be a positive number.")
        else:
            break
    except:
        print("Enter a valid balance.")


items = ["iPhone 15","iPods","Stainless Steel Fridge","Coffee Pod Organizer","Knife Set","Air Purifier", "Apple Watch", "Cat Tree", "Cat Water Fountain", "Smart Dog Collar"
"Water Bottle", "Korean Face Cream", "Protein Powder", "Eye Mask", "Necklace", "Hiking Boots", "Dell XPS Laptop"]



quality = ["poor", "mediocre", "good", "excellent"]

while balance >= 0:
    print("Welcome to your futuristic shopping experience ", + name)
    print("You currently have " + balance + "in your account")
    break




def deposit(amount):
    account += amount

def withdraw(amount):
    account -= amount

def transfer(amount):
    account -= amount
    account1 += amount



