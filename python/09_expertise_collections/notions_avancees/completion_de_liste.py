#          0        1         2          3          4       5
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé', 'Martin']

longueur_noms = []
for nom in noms :
    longueur_noms.append(len(nom))
print(longueur_noms)

longueur_noms = [len(nom) for nom in noms]  # code équivalent au précédent plus concis
print(longueur_noms)

longueur_noms = [len(nom) for nom in noms if len(nom) < 9]  # on peut conditionner 
print(longueur_noms)

noms_avec_e = [nom for nom in noms if "e" in nom]
print(noms_avec_e)

longueur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]  # on conditionne la valeur elle-même
print(longueur_noms)

a = [i for i in range(11) if (i//2)*2 == i] # on affiche les nombres pairs
print(a)
a = [i for i in range(11) if (i//2)*2 != i] # on affiche les nombres impairs
print(a)

b = [(i, True if (i//2)*2 == i else False) for i in range(11)]
print(b) 