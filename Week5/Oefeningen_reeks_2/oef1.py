medical_devices = ["X-ray", "MRI", "Epoch"]

device = input("Welke machine wil je toevoegen? ")

try:
    if device in medical_devices:
        raise ValueError("Apparaat is al in lijst")
    else:
        medical_devices.append(device)
except Exception as e:
    print(e)
finally:
    print(medical_devices)



