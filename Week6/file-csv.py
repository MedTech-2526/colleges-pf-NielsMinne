# import csv

	
# name = input("What's your name? ")
# location = input("Where do you live? ")
 
# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "location"])
#     writer.writerow({"name": name, "location": location})


	
import csv
 
students = []
 
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "location": row["location"]})
 
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['location']}")