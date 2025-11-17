"""
Working with Datasets in Python
Day 2: Lecture Code

Chloe Simanek
"""

# Import the data 

data = []

with open('covid.csv') as file:
    next(file)  
    for line in file:  
        line = line.strip()
        fields = line.split(",")
        data.append(fields)  

# Most cases 

most_cases = 0
state_with_most_cases = ""
for row in data:
    cases = float(row[2])
    if cases > most_cases:
        most_cases = cases
        state_with_most_cases = row[1]

print(f"{state_with_most_cases} had {most_cases} cases")

# Least cases 

least_cases = float('inf')
state_with_least_cases = ""
for row in data: 
    cases = float(row[2])
    if cases < least_cases:
        # Check least cases 
        print(least_cases)
        least_cases = cases
        state_with_least_cases = row[1]
print(f"{state_with_least_cases} had {least_cases} cases")

# Another way to import data

dates = []
states = []
positive_cases = []

with open('covid.csv') as file:
    next(file)  
    for line in file:
        fields = line.strip().split(",")
        dates.append(fields[0])
        states.append(fields[1])
        positive_cases.append(float(fields[2]))

most_cases = max(positive_cases)
index = positive_cases.index(most_cases)
state_with_most_cases = states[index]
print(f"{state_with_most_cases} had {most_cases} cases" )

# Repeat with least cases