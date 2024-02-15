#          0        1         2          3          4       5
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé', 'Martin']

a = [True, True, False, False]
print(any(a))   # il faut au moins 1 élément True pour retourner True
print(all(a))   # il faut tous les éléments True pour retourner True

found = False   # code initial pour savoir s'il y a un nom avec un z
for nom in noms :
    if "z" in nom.lower():
        found = True
        break
if found :
    print("Trouvé")
else :
    print("Non trouvé")

nom_avec_un_z = [True if "z" in nom.lower() else False for nom in noms] # cheminement d'un code simplifié par complétion de liste
print(nom_avec_un_z)
print(any(nom_avec_un_z))   # application du any (ou all)

nom_avec_un_z_existe = any([True if "z" in nom.lower() else False for nom in noms]) # code final équivalent au code initial
if nom_avec_un_z_existe :
    print("Trouvé")
else :
    print("Non trouvé")