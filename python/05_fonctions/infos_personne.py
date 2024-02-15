
""" recuperer_et_afficher_infos_personnes
    -> recuperer_infos_personne
    -> afficher_infos_personne
        -> est_majeur """

def est_majeur(age):
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(numero):
    nom_info = input(f"Nom de la personne {numero} ? ")
    age_info = int(input(f"Age de la personne {numero} ? "))
    return nom_info, age_info

def afficher_info_personne(numero, nom, age):
    print(f"La personne {numero} se nomme {nom} et a {age} ans.")
    print(f"Dans son nom, il y a {len(nom)} caractères.")
    if est_majeur(age):
        print(f"{nom}, vous êtes majeur.")
    else:
        print(f"{nom}, vous êtes mineur.")
    print()

def recuperer_et_afficher_infos_personnes(numero_personne):
    nom_personne, age_personne = recuperer_infos_personne(numero_personne)
    afficher_info_personne(numero_personne, nom_personne, age_personne)

#----------------------------------------------------------------------------

nb_personnes = 2

for i in range(nb_personnes):
    recuperer_et_afficher_infos_personnes(i+1)


