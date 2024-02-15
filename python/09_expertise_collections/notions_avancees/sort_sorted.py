#            0          1       2       3         4
noms = ['Christophe', 'Zoé', 'Jean', 'Sophie', 'Martin']

""" sort trie par défaut :
        - par ordre alphabétique pour du str
        - du + petit au + grand pour du int 

    noms.sort()     
        -> modification dite "inplace" (la liste originale est modifiée)
    noms_tries = sorted(noms)       
        -> on crée une nouvelle liste 
"""

print(noms)

noms.sort() # tri alpha croissant
print(noms)

noms_tries = sorted(noms, reverse = True) # tri alpha décroissant
print(noms_tries)

noms.sort(key = lambda nom : len(nom)) # tri par longueur de nom croissant
print(noms)

noms_tries = sorted(noms, key = lambda nom : len(nom), reverse = True)  # tri par longueur de nom décroissant
print(noms_tries)

print(noms[:4:2])
print(noms_tries[::-3])