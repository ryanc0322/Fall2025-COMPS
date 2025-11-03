"""

Day 2 

"""

with open('covid.csv') as file:
    lines = file.readlines()  
    lines = lines[1:]         

data = []  

for line in lines:
    line = line.strip()     
    fields = line.split(",") 
    data.append(fields)   

# YOUR CODE BELOW

most_cases = 0
state_with_most_cases = ""
for row in data:
    cases = float(row[2])
    if cases > most_cases:
        most_cases = cases
        state_with_most_cases = row[1]

print(f"{state_with_most_cases} had {most_cases} cases")

least_cases = float('inf')
state_with_least_cases = ""
for row in data: 
    cases = float(row[2])
    if cases < least_cases:
        least_cases = cases
        state_with_least_cases = row[1]
print(f"{state_with_least_cases} had {least_cases} cases")

total_cases = 0
for row in data: 
    cases = float(row[2])
    total_cases += cases

print(total_cases)

average = total_cases / 50
print(average)

percent = most_cases / total_cases
print(percent)