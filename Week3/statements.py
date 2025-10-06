#natch case statement
day = input("Enter the day of the week: ")
day = day.lower().strip()
print(day)

match day:
    case "maandag":
        print("Het is maandag, begin van de week!")
    case "vrijdag":
        print("Het is vrijdag, bijna weekend!")
    case "zondag":
        print("Het is zondag, tijd om te ontspannen.")
    case _:
        print("Dit is geen correcte invoer.")
    