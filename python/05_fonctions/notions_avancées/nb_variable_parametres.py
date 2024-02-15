# NOMBRE VARIABLE DE PARAMÈTRES

# '*' permet au paramètre de devenir variable, exemple :
def somme(titre, *notes): 
    print(f"Titre : {titre}")
    resultat = 0
    for n in notes :
        resultat += n
    return resultat

print(somme("Somme des notes", 2, 4, 15, 18, 7, 19))

# '**' permet d'assigner une clé, exemple :
def somme(titre, **notes): 
    print(f"Titre : {titre}")
    resultat = 0
    for n in notes.values() :   # il faut ajouter .values() pour récupérer les valeurs
        resultat += n
    return resultat

print(somme("Somme des notes", math=12, geo=14, anglais=19))
