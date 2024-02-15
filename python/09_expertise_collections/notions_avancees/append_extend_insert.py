noms = ['Jean', 'Sophie', 'Martin']
noms_supplementaires = ['Christophe', 'Zoé']
noms_supplementaires_2 = ['Pierre', 'Paul']
noms_supplementaires_3 = ['Titi', 'Laura']
noms_supplementaires_4 = ['Clément', 'Jenny']

print(noms)

noms = noms + noms_supplementaires # concaténation de listes

for nom in noms_supplementaires_2: # méthode append
   noms.append(nom)

noms.extend(noms_supplementaires_3) # méthode extend

noms += noms_supplementaires_4 # méthode +=

noms = ['Tata'] + noms # ajoute une valeur en tête de liste
noms.insert(6, 'Toto') # ajoute une valeur à l'index 6

print(noms)