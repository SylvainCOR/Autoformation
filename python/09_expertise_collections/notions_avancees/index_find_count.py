#          0        1         2          3          4       5
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé', 'Martin']

element_cherche = 'Martin'

if element_cherche in noms :
   print(f"L'élément cherché est à l'index : {noms.index(element_cherche, 3)}")   # index de début = 3
else :
   print("Erreur : l'élément n'est pas dans la collection")

print()
nb_occurence = noms.count(element_cherche)
print(f"Nombre d'occurences : {nb_occurence}")
if nb_occurence > 0 :
    index_occurence = 0
    for i in range(nb_occurence) :
        index_occurence = noms.index(element_cherche, index_occurence)
        print(f"{element_cherche} trouvé à {index_occurence}")
        index_occurence += 1
else :
    print("Erreur : l'élément n'est pas dans la collection")

print()
chaine = '-'.join(noms)
position = chaine.find(element_cherche) # find fonctionne uniquement sur des chaines de caractères de la même façon que index sur les collections
print(chaine)
print(f"{element_cherche} commence à l'index {position} de la chaîne de caractères") 
