


# names = []

# for _ in range(3):
#     name = input("Wat is je naam? ")
#     names.append(name)

# for name in sorted(names):
#     print(name)


# name = input("Wat is je naam? ")

#Write
# file = open("namen.txt", "w")
# file.write(name)
# file.close()

#Append
# with open("namen.txt", "a") as file:
#     file.write(f"{name}\n")

#Read
# with open("namen.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hallo,", line.strip())

with open("namen.txt", "r") as file:
    for line in file:
        print("Hallo", line.strip())





