# List
# Geordend en veranderlijk (Mutable) verzameling van elementen

list_example = [1, 35, 48, 65, 5]
print(list_example)

#Een lijst maken met list() functie
list_example2 = list([1,2,3,4,5])
print(list_example2)

#Toegang tot lijst element (via index)
# print(list_example[1])
# print(list_example[3])

# print(list_example[-1])

#slicen
sub_list = list_example[1:3] #Haalt elementen op van index 1 tot en met 2, 3 niet inbegrepen
print(sub_list)

#Merge
list1 = [1,2,3]
list2 = [4,5,6]

merged_list = list1 + list2
print(merged_list)

#Soorten methoden 
# append() -> Voegt een element toe aan het einde van de lijst
#remove() -> Verwijder het eerste voorkomen van een element
#pop() -> Verwijdert het laatste element (of een specifieke index)
#extend() -> Voegt meerdere elementen toe aan een lijst.
#insert() -> Voegt element toe aan specifieke index
#sort() -> Sorteert de lijst op plaats
#reverse() -> Draait de lijst om.

#Append
list_example3 = [1,2,3]
list_example3.append(10)
print(list_example3)

list_names = ["Wajih", "Tom", "Kubra","Kubra", "Zeno", " Indra"]
list_names.append("Niels")
list_names.append(6)
print(list_names)

#pop
list_names.pop()
print(list_names)

#remove()
list_names.remove("Kubra")
print(list_names)

#extend()
list_names.extend(["Jonas", "Thor"])
print(list_names)

fruit = ["Appel", "Mango", "Dragonfruit", "Vijgen", "Druiven"]
fruit.insert(2, "Kiwi")
print(fruit)

#sort
fruit.sort()
print(fruit)

#reverse()
fruit.reverse()
print(fruit)

#list unpacken -> van elke item een aparte variable maken
hobbies = ["Voetbal", "Boksen", "Kickboxen", "Lopen"]
hobby1 , hobby2, hobby3, hobby4 = hobbies
print(hobby1)
print(hobby3)

#items overslaan
football, *other_hobbies  , run = hobbies
print(football)
print(other_hobbies)
print(run)


