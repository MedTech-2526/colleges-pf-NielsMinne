#integer
age = 19
print(age)

#float 
height = 1.75
print(height)

#typecasting
#float to int 
decimal_number = 7.99
whole_number = int(decimal_number)
print(whole_number)

# int to float
whole_number = 5
decimal_number = float(whole_number)
print(decimal_number)

#int en float naar string
age = 25
height = 1.75
age_str = str(age)
height_str = str(height)

print(age_str)
print(height_str)

#van string naar int en float
number_string = "45"
number_string_float = "45.6"
number = int(number_string)
number_float = float(number_string_float)
print(number)
print(number_float)


#user input en typecasting om te vermenigvuldigen
#1. vraag een nummer
number = int(input("Kies een nummer... "))

#2. Vermenigvuldig nummer met 10
result = number * 10

#3. print naar console
print("Jou number vermenigvuldigd met 10 is:", result)
