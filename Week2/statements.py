number = int(input("Geef een getal in: "))

if number > 10:
    print("Het getal is groter dan 10")

#if - else statement

if number > 0:
    print("Het getal is positief!")
    print()
else:
    print("Het getal is negatief!")
    print("nog een lijntje")

# #waarom niet alleen if's
if number >= 0:
    print("Het getal is positief!")

if number < 0:
    print("het getal is negatief!")

if number == 0:
    print("Het getal is nul.")


# elif statement
if number >= 0:
    print("het getal is positief.")
elif number < 0:
    print("Het getal is negatief.")
else:
    print("Het getal is nul!")

#grade
#let op volgorde van hoog naar laag

grade = int(input("Geef je cijfer in: "))

if grade >= 90:
    print("Je hebt een A.")
elif grade >= 80:
    print("Je hebt een B.")
elif grade >= 70:
    print("Je hebt een C.")
elif grade >= 60:
    print("Je hebt een D.")
else:
    print("Je hebt een F.")

    print