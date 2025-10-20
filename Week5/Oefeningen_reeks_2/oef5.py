devices = []

def update_device_status(device, status, devices):
    temp_device = {
        "name" : device,
        "status" : status
    }
    devices.append(temp_device)
    return devices

print(update_device_status("X-ray", "Kapoet", devices))
print(update_device_status("MRI", "Kapot", devices))