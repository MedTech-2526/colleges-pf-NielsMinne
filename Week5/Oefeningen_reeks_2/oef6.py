patients = [
    {
    "name": "Jane Doe",
    "therapy": "Chemotherapy"
    },
      {
    "name": "John Doe",
    "therapy": "Physical Therapy"
    },
]

def print_treatments(patients):
    for patient in patients:
        print(f"Patient {patient["name"]} is undergoing {patient["therapy"]}")


print_treatments(patients)