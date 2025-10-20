# number = int(input("Voer een getal in: "))

# if n < 5:
#     number = int(input("Voer een getal in: "))
#     if n < 5:
#         number = int(input("Voer een getal in: "))
#         if n  5 

# while True:
#     number = int(input("Voer een getal in: "))
#     if number > 5: 
#         break
#     else:
#         print("Dit is niet boven 5")

# while True:
#     number = int(input("Geef een positief nummer? "))
#     if number < 0:
#         continue 
#     else:
#         break

#

# while True:
#     n = int(input("Hoeveel keer moet ik Harman printen? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Harman")



# def main():
#     number = get_numbers()
#     blub(number)

# def get_numbers():
#     while True:
#         n = int(input("Hoeveel keer moet ik blub printen? "))
#         if n > 0:
#             return n
        
# def blub(n):
#     for _ in range(n):
#         print("Blub")

# if __name__ == "__main__":
#     main()

# students = ["Lucas", "Jonas", "Milo", "Yoshka"]

# for student in students:
#     print(student)

# # print(len(students))

# for i in range(len(students)):
#     print(f"{i + 1} {students[i]}")

#None
# def check_numbers(n):
#     if n < 0:
#         return None
#     else:
#         return n 

# print(check_numbers(-2))
# print(check_numbers(5))


def main():
    x = get_int()
    print(f" x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("Je getal is geen nummer")
        else:
            break
    
    return x

main()
