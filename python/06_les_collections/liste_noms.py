
noms =[]

while True :
    nom = input("Nom de la personne : ")
    if nom == "" :
        break
    noms.append(nom)

print()
print("Liste des noms : ")

noms.sort() # tri alphabétique (de A à Z puis de a à z, cf table ASCII)
for nom in noms :
    print(nom)



