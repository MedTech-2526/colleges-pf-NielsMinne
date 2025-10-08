urgency = input("Urgentie? ").strip().lower()
age = int(input("Leeftijd? "))

if urgency == "hoog":
    message =  "Meteen behandelen!"
elif urgency == "medium" and age > 65:
    message = "Patient krijgt voorrang!"
else:
    message = "Ga dood."

print(message)

