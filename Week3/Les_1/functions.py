def hello():
    print("Hallo")

hello()

def greet(name = "Anon"):
    print("Hallo, " + name)

greet("Yoshka")
greet()

#functie met meerdere argumenten
def introduce(name , age):
    print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

name = input("What is your name ")
age = int(input("What is your age? "))

introduce(name, age)

#functie die data returned
def add(a,b):
    return a + b

result = add(5,3)
print(result)
print(add(4,3))

#lijst printen van namen (*args) -> meerdere argument
def print_names(*names):
    for name in names:
        print(name)

print_names("Niels", "Rana", "Tom", "Josephat")


