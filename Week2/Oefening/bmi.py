#alles opvragen
weight = float(input("Wat is uw gewicht? "))
length = float(input("Wat is uw lengte (in m)? "))

#berekening
bmi = weight / (length * length)
bmi = round(bmi, 2)

#printen 
print(f"Uw bmi is {bmi}")