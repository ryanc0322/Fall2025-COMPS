"""

Day 1 

The Data
-------- 

Take a look at the covid.csv file, briefly describe what you see. What data is there? Columns? Rows? Is there anything else you notice?
YOUR ANSWER HERE

** other question here ** 
YOUR ANSWER HERE

Reading the Data
----------------

What does the error message say? Copy it below. What does it mean? 
YOUR ANSWER HERE

Looking at the Data
-------------------
Printing 
1. YOUR ANSWER HERE
2. YOUR ANSWER HERE
3. YOUR ANSWER HERE

Challenge: YOUR ANSWER HERE

"""

# file = open("../covid.csv")
# data = file.read()
# print(data)
# file.close() 

with open('covid.csv') as file:
    lines = file.readlines()  # Read all lines into a list
    lines = lines[1:]         # Skip the first row (header)

data = []  # Empty list to store each row

for line in lines:
    line = line.strip()     
    fields = line.split(",") 
    data.append(fields)      

# YOUR CODE BELOW

# print("Row 3:", data[2])

# for row in data:
    # print(row[1])
    # if row[1] == 'MN':
    #     print(row[2])

# print("Row 3, Column 2:", data[2][1])


"""
Day 2 
"""