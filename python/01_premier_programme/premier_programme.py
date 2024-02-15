
def afficher_info_personne(nom, age):
    print()
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.") 
    print("L'an prochain vous aurez " + str(age+1) + " ans.")

    if age == 1 or age == 2 :
        print("Vous êtes bébé")
    elif age < 10 :
        print("Vous êtes enfant")
    elif age == 17 :
        print("Vous êtes presque majeur")
    elif 12 <= age < 18 :
        print("Vous êtes adolescent")
    elif age < 17 :
        print("Vous êtes mineur")
    elif age == 18 :
        print("Vous êtes tout juste majeur")
    elif age > 60 :
        print("Vous êtes senior")
    else:
        print("Vous êtes majeur")
    print()

def demander_age(nom_personne):
    age = 0
    while age == 0:
        reponse = input(nom_personne + " quel âge avez-vous ? ")
        try:
            age = int(reponse)
        except ValueError:
            print("Erreur: Vous devez entrer un nombre entier!")
    return age

def demander_nom():
    rep_nom = ""
    while rep_nom == "":
        rep_nom = input("Quel est votre nom ? ")
    return rep_nom

#------------------------------------------------------

# nom1 = demander_nom()
# nom2 = demander_nom()

# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# afficher_info_personne(nom1, age1)
# afficher_info_personne(nom2, age2)

NB_PERSONNES = 3

for i in range (0, NB_PERSONNES):
    nom = "personne " + str(i+1)
    age = demander_age(nom)
    afficher_info_personne(nom, age)

