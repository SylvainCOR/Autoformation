def chaine_contient_chiffre(chaine):
    # for c in chaine :
    #     if c.isdigit():
    #         return True
    # return False
    return any([c.isdigit() for c in chaine])   # équivalent au code précédent

nom = input("Quel est votre nom ? ")
if nom == "" :
    print("Le nom est vide")
elif chaine_contient_chiffre(nom) :
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else :
    print(f"Bonjour {nom}")