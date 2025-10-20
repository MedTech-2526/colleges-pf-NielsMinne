
patients_info = [
    ("John Doe", 45, "Diabetes"),
    ("Jane Smith", 37, "Hypertension")
]

def print_patient_info(patients):
    for patient_info in patients_info:
        print(f"Name: {patient_info[0]}")
        print(f"Age: {patient_info[1]}")
        print(f"Condition: {patient_info[2]}")

print_patient_info(patients_info)