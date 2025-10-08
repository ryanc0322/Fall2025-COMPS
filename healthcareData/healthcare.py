'''
healthcare.py

Chloe Simanek and Ava Amthauer

Description:
'''


'''
Part 1: Know Your Data
'''

filename = "healthcare_data.csv"

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
admission_types = []
discharge_dates = []
medications = []
test_results = []
# TODO: Add the rest of the fields  

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
        admission_types.append(fields[8])
        discharge_dates.append(fields[9])
        medications.append(fields[10])
        test_results.append(fields[11])

# Print the first row 
print(names[0], ages[0], genders[0], blood_types[0], medical_conditions[0], dates_of_admission[0], doctors[0], hospitals[0], admission_types[0], discharge_dates[0], medications[0], test_results[0])
# Print all medical conditions 
# for condition in medical_conditions:
    # print(condition)

'''
Part 2: What Can Your Data Tell You?
'''

# TODO: Demographics: age and gender
under_18 = 0
between_18_and_30 = 0
between_30_and_50 = 0
between_50_and_70 = 0
over_70 = 0
for age in ages:
    if age < 18:
        under_18 += 1
    if age >= 18 and age < 30:
        between_18_and_30 += 1
    if age >= 30 and age < 50:
        between_30_and_50 += 1
    if age >= 50 and age < 70:
        between_50_and_70 += 1
    if age >= 70:
        over_70 += 1

total = len(ages)

under_18_percent = (under_18 / total) * 100
between_18_and_30_percent = (between_18_and_30 / total) * 100
between_30_and_50_percent = (between_30_and_50 / total) * 100
between_50_and_70_percent = (between_50_and_70 / total) * 100
over_70_percent = (over_70 / total) * 100

# print(f"Percentage of patients under 18: {under_18_percent:.2f}%")
# etc.

female = 0
male = 0
for gender in genders:
    if gender == 'Female':
        female += 1
    elif gender == 'Male':
        male += 1

female_percent = (female / total) * 100
male_percent = (male / total) * 100

# print(f"Percentage of female patients: {female_percent:.2f}%")
# print(f"Percentage of male patients: {male_percent:.2f}%")

# TODO: Hospital representation

northview_medical = 0
riverside_clinic = 0
henderson_johnson_hospital = 0
greenfield_health = 0
summit_regional = 0

for hospital in hospitals:
    if hospital == "Northview Medical":
        northview_medical += 1
    elif hospital == "Riverside Clinic":
        riverside_clinic += 1
    elif hospital == "Henderson-Johnson Hospital":
        henderson_johnson_hospital += 1
    elif hospital == "Greenfield Health":
        greenfield_health += 1
    elif hospital == "Summit Regional":
        summit_regional += 1

northview_medical_percent = (northview_medical / total) * 100
riverside_clinic_percent = (riverside_clinic / total) * 100
henderson_johnson_hospital_percent = (henderson_johnson_hospital / total) * 100
greenfield_health_percent = (greenfield_health / total) * 100
summit_regional_percent = (summit_regional / total) * 100

# NOTE: Discussion 

'''
Part 3: Visualizing the Data
'''

'''
Henderson-Johnson Hospital wants to know more about their patients. 
You have been asked to create a report that includes the following
visualizations:
- Number of admissions over time
- Average length of stay by admission type
- Total number of each condition
'''

'''
The doctors there also want to know if cancer is related to age, so
they can predict which patients are at higher risk. Create a
visualization that shows the number of cancer patients by age group.
'''



