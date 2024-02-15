import random

#---CONSTANTES---

NOMBRE_MIN = 1
NOMBRE_MAX = 50
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

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

#---PROGRAMME_BOUCLE_WHILE---

vies = NB_VIES
nombre = 0

while not nombre == NOMBRE_MAGIQUE and vies > 0 :
    print(f"Il vous reste {vies} vies...")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE :
        print("Bravo, vous avez trouvé !")
    elif nombre > NOMBRE_MAGIQUE :
        print("Le nombre magique est plus petit !")
        vies -= 1
    else :
        print("Le nombre magique est plus grand !")
        vies -= 1

if vies == 0 :
    print(f"Vous avez perdu, le nombre magique était {NOMBRE_MAGIQUE} !")