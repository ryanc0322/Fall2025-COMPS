"""
Working with Datasets in Python
Day 2: Lab

Chloe Simanek

Student name: *****
"""

# Import the data 

data = []

with open('covid.csv') as file:
    next(file)  
    for line in file:  
        line = line.strip()
        fields = line.split(",")
        data.append(fields)  

# ----------------------------------------------------------

# Total positive cases 

# YOUR CODE HERE

# ----------------------------------------------------------

# Average number of positive cases

# YOUR CODE HERE

# ----------------------------------------------------------

# Do you think using the average in a report of positive
# cases in the United States makes sense? Why or why not?

# YOUR ANSWER HERE

# ----------------------------------------------------------

# What other data would you like to have when looking at
# this dataset? 

# YOUR ANSWER HERE

# ----------------------------------------------------------

# Percent of total cases the state with the most
# cases made up

# YOUR CODE HERE

# ----------------------------------------------------------