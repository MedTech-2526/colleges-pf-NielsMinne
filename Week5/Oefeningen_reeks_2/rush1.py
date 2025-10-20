name = input("Wat is uw naam? ")

name = name.strip()
name = name.title()

age = int(input("Wat is uw leeftijd?"))

favourite_language = input("Wat is je favoriete programmeertaal? ").strip().title()


print(f"Hallo {name}! jij bent {age} jaar en jouw favoriete taal is {favourite_language}")

if age < 12:
    print("Je bent nog jong om te programmeren, maar goed bezig!")
elif age >= 12 and age <= 18:
     print("Top! Je zit in de perfecte leeftijd om veel te leren.")
elif age > 18 and age <= 40:
     print("Je hebt de kracht en logica om een expert te worden.") 
else:
     print("Je bewijst dat leren programmeren geen leeftijd kent.") 

if favourite_language == "python":
     print("Goede keuze! Python is geweldig.")
