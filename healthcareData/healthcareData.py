'''
healthcare.py

Chloe Simanek and Ava Amthauer

Description:
'''
from datetime import datetime
import matplotlib.pyplot as plt

'''
Part 1: Know Your Data
'''

filename = "healthcare_data.csv"

# Lists to store each column
names = []
ages = []
# TODO: Continue the lists below

# Open the file and read the data
with open(filename) as file:
    next(file)  # Skip the header line
    for line in file: 
        fields = line.strip().split(",") 
        names.append(fields[0])
        ages.append(int(fields[1]))
        # TODO: Continue appending to the lists below

# TODO: Print the first row 

# TODO: Print the medical conditions

'''
Part 2: What Can Your Data Tell You?
'''

# TODO: Demographics: age and gender

# TODO: Hospital representation

'''
Part 3: Visualizing the Data
'''

# TODO: Admissions per year at Henderson-Johnson Hospital

# TODO: Cancer patients by age group at Henderson-Johnson Hospital


