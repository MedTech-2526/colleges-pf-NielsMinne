#Set

# een set maak je aan met accolades
new_set = {1,2,3,4,5}
print(new_set)

new_set2 = set([1,2,3,4,5])
print(new_set2)

#LET OP - Een lege set maak je aan met set() niet met {}
empty_set = set() #Een lege set
empty_dict = {} #Dit maakt een lege dictionary

#elementen toevoegen of verwijderen

#toevoegen - add()
number_set = {1, 5, 8 ,10}
number_set.add(4)
print(number_set)

number_set.update([5,6,7])
print(number_set)

#verwijderen
number_set.remove(4)
print(number_set)

number_set.discard(4) # geeft geen foutmelding als het getal ontbreekt

#pop()
removed_element = number_set.pop() # Verwijder het eerste element
print("Verwijderd:", removed_element)


#Set operations

set1 = {1,2,3}
set2 = {3,4,5,6}

#Union 
union_set = set1 | set2
print(union_set)

union_set2 = set1.union(set2)
print(union_set2)

#Intersection -> Alle gemeenschappelijk element
intersect_set = set1 & set2
print(intersect_set)

intersect_set2 = set1.intersection(set2)
print(intersect_set2)

#difference -> Geef de elementen terug die alleen in een set zitten 
diff_set = set1 - set2
print(diff_set)

diff_set2 = set1.difference(set2)
print(diff_set2)

#controle of een element in set zit
print(2 in set1) # true
print(7 in set2) # false


