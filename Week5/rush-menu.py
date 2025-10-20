def greet():
    print("Hallo, Welkom in het programma!")

def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a +b
    print(f"The sum is: {result}")

def multiply_numbers(number_a, number_b):
    multiplication = number_a * number_b
    print(f"The product is: {multiplication}")

def quit_program():
    print("Goodbye!")
    exit()


def show_menu():
    print("\n=== Simple Menu ===")
    print("1. Greet")
    print("2. Add numbers")
    print("3. Multiply Number")
    print("4. Quit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            greet()
        elif choice == "2":
            add_numbers()
        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            multiply_numbers(a,b)
        elif choice == "4":
            quit_program()
        else:
            print("Invalid Choice, Please try again")


main()