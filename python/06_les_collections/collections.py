# Collection : (Tableaux : Array), listes, tuples
# Tuple () : immuable
# Liste [] : altérable


#----------- TUPLES ------------------------------

personnes = ("Jean", "Pierre", "Paul", "Jacques")

print(len(personnes))
print(personnes[-1]) 

for i in range(0, len(personnes)):
    print(personnes[i])

for i in personnes :
    print(i)
    print(len(i))
    print(i[0] + i[1])


#----------- LISTES ------------------------------

personnes = ["Jean", "Pierre", "Paul", "Jacques"]
nouvelle_personne = "David"

print(personnes)
personnes.append(nouvelle_personne)
del personnes[2]
print(personnes)

def afficher_personnes(liste):
    for i in liste :
        print(i)

afficher_personnes(personnes)


def modifier_valeur(a):
    a[0] = 10

test = [0, 1, 2, 3]
print(test)
modifier_valeur(test)
print(test)


#----------- FONCTIONS ET TUPLES ------------------------------

def obtenir_information():
    return "Clara", 1.75, 25

def afficher_informations(nom, taille, age):
    print(f"Informations :   Nom : {nom}   Taille : {taille}   Age : {age}")

infos = obtenir_information()
afficher_informations(*infos) # '*' pour séparer les paramètres. (*infos) <=> (infos[0], infos[1], infos[2])

print("Nom : " + infos[0])
print(f"Taille : {infos[1]}")
print(f"Age : {infos[2]}")

print(infos) # affiche un tuple (1 seule valeur)
print(*infos) # affiches les valeurs du tuple séparement (unpack tuple)


#----------- SLICES ------------------------------

personnes = ("Jean", "Pierre", "Paul", "Jacques", "Clara", "Alice")

# fonctionnement de l'index [start : stop : step]
# start inclusif, stop exclusif

print(*personnes[0:3]) # affiche: Jean Pierre Paul
print(*personnes[:]) # affiche: Jean Pierre Paul Jacques Clara Alice
print(*personnes[1::2]) # affiche: Pierre Jacques Alice
print(*personnes[::-1]) # affiche: Alice Clara Jacques Paul Pierre Jean
print(*personnes[::-2]) # affiche: Alice Jacques Pierre

for i in personnes[:]:
    print(i[::-1])




