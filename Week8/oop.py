class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
        if not patronus:
            raise ValueError("No Patronus")
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is in house {self.house}"
    
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

        
def main():
    student = get_student() # (Niels, Hufflepuff)
    print(student)
    print(student.charm())
    # print(f"{student.name} is in house {student.house}")

def get_student():
    while True:
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        try:
            return Student(name, house, patronus)
        except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    main()