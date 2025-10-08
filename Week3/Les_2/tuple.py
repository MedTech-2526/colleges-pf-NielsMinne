#Tuple

# Een tuple maken met haakjes
tuple_example = (1,2,3,4,10,6)
print(tuple_example)

#tuple() functie
tuple_example2 = tuple([1,2,3,4,5])
print(tuple_example2)

#LET OP 
tuple_example3 = (5,) 
tuple_2 = (5) #integer

print(tuple_example[2])

#slicing zelfde als list

#tuple mergen 
tuple1 = (1,2,3)
tuple2 = (4,5,6)
merged_tuple = tuple1 + tuple2

print(merged_tuple)

repeated_tuple = tuple1 * 2
print(repeated_tuple)

#tuple methoden
#count() -> Telt hoeveel keer de waarde voorkomt
#index() -> Geeft de index van de eerste keer dat de waarde voorkomt.add()

tuple_example4 = (1,2,3,2,4,2)

print(tuple_example4.count(2)) #output: 3
print(tuple_example4.index(3)) #output: 2

#unpacken zelfde als list
tuple_fruit = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = tuple_fruit
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry
