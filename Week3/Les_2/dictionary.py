#dictionary - object

patient = {
    "name": "Niels",
    "age": 32,
    "birthplace": "Brugge",
    "vaccinated": True
}

print(patient["vaccinated"])
print(patient.get("vaccinated"))

# print(patient["hospital"]) #zal een error geven
print(patient.get("hospital")) #zal None tonen als waarde

#toevoegen
patient["hospital"] = "Az. St-Lucas"
print(patient)

#verwijderen
del patient["hospital"]
print(patient)

#methoden
#keys() -> haalt alle keys op 
#values() -> Haalt alle values op 
#items() ->  Haalt zowel de key op als value
#update() -> Voegt een key-value pair toevoegen

#keys()
print(patient.keys())

#values()
print(patient.values())

#items()
print(patient.items())

#udpate() 
patient.update({"hobbies" : "Lui zijn"})
print(patient)

