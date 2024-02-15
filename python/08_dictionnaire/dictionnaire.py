
# Partie 1 : fonctionnement dictionnaire
personne = {'nom': 'Mélanie', 'age': 25, 'taille': 1.70}

print(personne)
print(personne['nom'])
print(personne['age'])

personne['poste'] = 'Développeur'
print(personne)

achat = ('choco', 'beurre', 'pain')
personne['achats'] = achat
print(personne)

for i in personne :
    print(f"clé : {i} - valeur : {personne[i]}")


# Partie 2 : comparaison liste/dictionnaire
# nom, age, taille
personnes = [
    ('Pierre', 25, 1.6),
    ('Paul', 29, 1.8),
    ('Paul', 35, 1.75),
    ('Jack', 16, 1.65),
]

def obtenir_info(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

# Jack
infos = obtenir_info('Jack', personnes)
print(*infos)

personnes_dico = {
    'Pierre': (25, 1.6),
    'Paul': (29, 1.8),
    'Paul': (35, 1.75),
    'Jack': (16, 1.65)
}

infos = personnes_dico.get('Paul')
if infos == None : # on peut remplacer par:  if not infos :
    print("Cet info n'existe pas)")
else:
    print(*infos)

