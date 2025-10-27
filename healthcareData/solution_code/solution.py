from datetime import datetime
import matplotlib.pyplot as plt

'''
Part 1: Know Your Data
'''

filename = "healthcare_data.csv"

# Lists to store each column
names = []
ages = []
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

# Open the file and read the data
with open(filename) as file:
    next(file)  # Skip the header line
    for line in file: 
        fields = line.strip().split(",") 
        names.append(fields[0])
        ages.append(int(fields[1]))
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

# ========== Part 1 Output ==========
print("Answer to Print the first row goes here")
print(names[0], ages[0], genders[0], blood_types[0], medical_conditions[0], dates_of_admission[0],
      doctors[0], hospitals[0], admission_types[0], discharge_dates[0], medications[0], test_results[0])
for i in range(5):
    print(medical_conditions[i])
print(len(names))

'''
Part 2: What Can Your Data Tell You?
'''


under_18 = 0
between_18_and_30 = 0
between_30_and_50 = 0
between_50_and_70 = 0
over_70 = 0

for age in ages:
    if age < 18:
        under_18 += 1
    elif age < 30:
        between_18_and_30 += 1
    elif age < 50:
        between_30_and_50 += 1
    elif age < 70:
        between_50_and_70 += 1
    else:
        over_70 += 1

total_patients = len(names)

under_18_percent = (under_18 / total_patients) * 100
between_18_and_30_percent = (between_18_and_30 / total_patients) * 100
between_30_and_50_percent = (between_30_and_50 / total_patients) * 100
between_50_and_70_percent = (between_50_and_70 / total_patients) * 100
over_70_percent = (over_70 / total_patients) * 100

# ========== Part 2.1: Demographics ==========
print("Answer to Demographics goes here")

print(f"Under 18: {under_18_percent:.2f}%")
print(f"18-30: {between_18_and_30_percent:.2f}%")
print(f"30-50: {between_30_and_50_percent:.2f}%")
print(f"50-70: {between_50_and_70_percent:.2f}%")
print(f"Over 70: {over_70_percent:.2f}%")

female = 0
male = 0
for gender in genders:
    if gender == 'Female':
        female += 1
    elif gender == 'Male':
        male += 1

female_percent = (female / total_patients) * 100
male_percent = (male / total_patients) * 100

print(f"Percentage of female patients: {female_percent:.2f}%")
print(f"Percentage of male patients: {male_percent:.2f}%")


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

northview_medical_percent = (northview_medical / total_patients) * 100
riverside_clinic_percent = (riverside_clinic / total_patients) * 100
henderson_johnson_hospital_percent = (henderson_johnson_hospital / total_patients) * 100
greenfield_health_percent = (greenfield_health / total_patients) * 100
summit_regional_percent = (summit_regional / total_patients) * 100

# ========== Part 2.2: Hospital Representation ==========
print("Answer to Hospital representation goes here")

print(f"Northview Medical: {northview_medical_percent:.2f}%")
print(f"Riverside Clinic: {riverside_clinic_percent:.2f}%")
print(f"Henderson-Johnson Hospital: {henderson_johnson_hospital_percent:.2f}%")
print(f"Greenfield Health: {greenfield_health_percent:.2f}%")
print(f"Summit Regional: {summit_regional_percent:.2f}%")

'''
Part 3: Visualizing the Data
'''


henderson_johnson_admission_dates = []
for i in range(len(dates_of_admission)):
    if hospitals[i] == "Henderson-Johnson Hospital":
        henderson_johnson_admission_dates.append(dates_of_admission[i])

converted_dates = []
for date in henderson_johnson_admission_dates:
    date = datetime.strptime(date, "%Y-%m-%d")
    converted_dates.append(date)

year_counts = {}
for date in converted_dates:
    year = date.year
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

sorted_years = sorted(year_counts.keys())
counts = [year_counts[y] for y in sorted_years]

# ========== Part 3.1: Admissions per year ==========
print("Answer to Admissions per year at Henderson-Johnson Hospital goes here")

plt.figure(figsize=(8, 4))
plt.plot(sorted_years, counts)
plt.title("Number of Admissions Per Year at Henderson-Johnson Hospital")
plt.xlabel("Year")
plt.ylabel("Number of Admissions")
plt.xticks(sorted_years)
plt.close()  # prevents pop-up in testing


cancer_ages = []
for i in range(len(ages)):
    if hospitals[i] == "Henderson-Johnson Hospital" and medical_conditions[i] == "Cancer":
        cancer_ages.append(ages[i])

age_groups = ["0-17", "18-29", "30-49", "50-69", "70+"]
age_counts = [0] * len(age_groups)

for age in cancer_ages:
    if age <= 17:
        age_counts[0] += 1
    elif age <= 29:
        age_counts[1] += 1
    elif age <= 49:
        age_counts[2] += 1
    elif age <= 69:
        age_counts[3] += 1
    else:
        age_counts[4] += 1

# ========== Part 3.2: Cancer by Age ==========
print("Answer to Cancer patients by age group at Henderson-Johnson Hospital goes here")

plt.figure(figsize=(8, 4))
plt.bar(age_groups, age_counts)
plt.title("Cancer Patients by Age Group at Henderson-Johnson Hospital")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.close()  # prevents pop-up in testing



# x=1      # W0311: bad indentation
# y=2      
# z = x + y 
# z   # W0104: pointless statement
# result = (x + y) * b
# 10 + 5  # W0106: expression not assigned
# a = 1; b = 2; c = a + b  # C0321: multiple statements on one line
