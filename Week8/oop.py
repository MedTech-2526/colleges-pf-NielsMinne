import random

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class Student(Wizard):
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        super().__init__(name)
        self.house = house
        if not patronus:
            raise ValueError("No Patronus")
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is in house {self.house}"
    
    def speak(self):
        return "Ik ben een student van Zweinstein"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case _:
                return "✨"
            
    @property
    def house(self):
        return self._house
        
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)

	
class Gryffindor(Student):
    def speak(self):
        return "Moed en lef! Ik ben een Gryffindor!"
 
class Slytherin(Student):
    def speak(self):
        return "Ambitie en sluwheid. Ik ben een Slytherin."
 
class Ravenclaw(Student):
    def speak(self):
        return "Wijsheid eerst! Ravenclaw, natuurlijk."
 
class Hufflepuff(Student):
    def speak(self):
        return "Loyaliteit en hard werk, dat is Hufflepuff!"


class Hat:
    _instance = None
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
 
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
 
    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)

def main():
    # student = Student.get()
    # print(student)
    # wizard = Wizard("Albus")
    # student = Student("Harry", "Gryffindor")
    # professor = Professor("Severus", "Defense Against the Dark Arts")
    student = Gryffindor("Harry", "Gryffindor", "maaktnietuit")
    print(student.speak())





if __name__ == "__main__":
    main()