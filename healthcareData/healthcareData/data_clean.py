import csv

hospitals = [
    "Northview Medical",
    "Riverside Clinic",
    "Henderson-Johnson Hospital",
    "Greenfield Health",
    "Summit Regional"
]

def assign_hospital(input_csv, output_csv):
    with open(input_csv, newline='', encoding='utf-8') as inf:
        rows = list(csv.DictReader(inf))

    total = len(rows)
    print(f"Total rows: {total}")

    for i, row in enumerate(rows):
        if i < 10000:
            row["Hospital"] = hospitals[0]  
        elif i >= 10000 and i < 25000:
            row["Hospital"] = hospitals[1]  
        elif i >= 25000 and i < 32000:
            row["Hospital"] = hospitals[2]
        elif i >= 32000 and i < 50000:
            row["Hospital"] = hospitals[3]
        elif i >= 50000:
            row["Hospital"] = hospitals[4]  

    fieldnames = list(rows[0].keys())
    with open(output_csv, 'w', newline='', encoding='utf-8') as outf:
        writer = csv.DictWriter(outf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

assign_hospital("healthcare_data.csv", "healthcare_data_new.csv")