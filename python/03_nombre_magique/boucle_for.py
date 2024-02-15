import random

#---CONSTANTES---

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 7

#---FONCTIONS---

def demander_nombre(nb_min, nb_max) :
    nombre_int = 0
    while nombre_int == 0 :
        nombre_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")
        try :
            nombre_int = int(nombre_str)
        except :
            print("ERREUR : Vous devez entrer un nombre. Réessayez!")
        else :
            if not nb_min <= nombre_int <= nb_max :
                print(f"ERREUR : Vous devez entrer un nombre compris entre {nb_min} et {nb_max}. Réessayez!")
                nombre_int = 0
    return nombre_int

#---PROGRAMME_BOUCLE_FOR---

gagne = False

for i in range(0, NB_VIES) :
    vies = NB_VIES-i
    print(f"Il vous reste {vies} vies...")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE :
        print("Bravo, vous avez trouvé !")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE :
        print("Le nombre magique est plus petit !")
    else :
        print("Le nombre magique est plus grand !")

if not gagne :
    print(f"Vous avez perdu, le nombre magique était {NOMBRE_MAGIQUE} !")