#Globals

	
balance = 0
 
def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)
 
def deposit(n):
    global balance
    balance += n
 
def withdraw(n):
    global balance
    balance -= n
 
if __name__ == "__main__":
    main()


#CONSTANT

MEOWS = 3

for _ in range(MEOWS):
    print("Meow")


#Filter
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Hermione", "house": "Gryffindor"},
]

def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for g in gryffindors:
    print(g["name"])