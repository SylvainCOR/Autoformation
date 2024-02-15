#          0        1         2          3          4
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé']

t = noms[0]  # sauvegarde Jean temporairement
noms[0] = noms[4]   # écrase et remplace Jean par Zoé dans noms
noms[4] = t  # remplace Zoé par Jean dans noms
print(noms)

noms[0], noms[4] = noms[4], noms[0] # équivalent au code précédent
print(noms)

noms_join = " / ".join(noms) # on rejoint tous les éléments dans une chaine str avec un séparateur
print(noms_join)

noms_split = noms_join.split(" / ") # on regroupe tous les éléments dans une liste à partir d'un séparateur
print(noms_split)