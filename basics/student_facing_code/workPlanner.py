import workInfo as wi 
'''
workPlanner.py

Ava Amthauer and Chloe Simanek and Jamal Omosun

Description: Program for delivery drivers to calculate their expected weekly income. 
Inspired by the "Work Planner" from the paper "Stakeholder-Centered AI Design: Co-Designing
Worker Tools with Gig Workers through Data Probes". 
'''

'''
Part 1: Getting Started with Variables
Define variables for base pay, location, days and more. 
It is best practice to name the variables after what exactly they are representing.
'''
# TODO: Fixed variables go here
# ie: pay = 7.25 

# TODO: Driver set variables go here 
# ie: cost_of_fuel = 2.95


'''
Part 2: Calculations
Use operators to estimate weekly income.
wi.checkList is a function that will calculate some multipliers for you.
You do not have to worry about what exactly is going on behind the scenes,
you will learn more about it later in the class.
'''
# Neighborhood and day multipliers
neighborhood_multiplier = wi.checkList(neighborhoods)
day_multiplier = wi.checkList(days)

# TODO: Your calculations go here


'''
Part 3: Tying it Together: User Input
Allow the driver to enter their preferences and see their estimated weekly income. 
You can comment out all the hard-coded variables that you used beforehand.
You can do this in VS code by using either Ctrl + / or Cmd + /.
'''
# TODO: Your code goes here 
