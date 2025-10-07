'''
healthcare.py

Chloe Simanek and Ava Amthauer

Description:
'''


'''
Part 1: Know Your Data
'''

filename = "healthcare_dataset.csv"

# Lists to store each column
names = []
ages = []
# NOTE: have them do the ones below
genders = [] 
blood_types = []
medical_conditions = []
dates_of_admission = []
doctors = []
hospitals = []
insurance_providers = []
billing_amounts = []
room_numbers = []
admission_types = []
discharge_dates = []
medications = []
test_results = []
# TODO: Add the rest of the fields  
# ?????????????? REMOVE SOME OF THIS DATA ??????????????

# Open the file and read the data
with open(filename) as file:
    next(file)  # Skip the header line
    for line in file:
        fields = line.strip().split(",") 
        names.append(fields[0])
        ages.append(int(fields[1]))
        # NOTE: have them do the ones below
        genders.append(fields[2])
        blood_types.append(fields[3])
        medical_conditions.append(fields[4])
        dates_of_admission.append(fields[5])
        doctors.append(fields[6])
        hospitals.append(fields[7])
        insurance_providers.append(fields[8])
        billing_amounts.append(fields[9])
        room_numbers.append(fields[10])
        admission_types.append(fields[11])
        discharge_dates.append(fields[12])
        medications.append(fields[13])
        test_results.append(fields[14])

# Print the first row 
print(names[1], ages[1], genders[1], blood_types[1], medical_conditions[1], dates_of_admission[1], doctors[1], hospitals[1], insurance_providers[1], billing_amounts[1], room_numbers[1], admission_types[1], discharge_dates[1], medications[1], test_results[1])  # add other fields here if needed

# Print all medical conditions 
# for condition in medical_conditions:
    # print(condition)

'''
Part 2: What Can Your Data Tell You?
'''

# Demographics 

# Conditions

# Hospital / Doctor representation

# NOTE: Discussion 

'''
Part 3: Visualizing the Data
'''

# Condition by age group
# Treatment
