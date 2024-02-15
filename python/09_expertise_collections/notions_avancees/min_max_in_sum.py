#          0        1         2          3          4
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé']
ages = [21, 20, 30, 25, 22]

print(min(ages))  # mini/maxi valeur numérique
print(max(ages))

print(min(noms))  # mini/maxi valeur alphabétique (! pas une bonne pratique)
print(max(noms))

if 'Jean' in noms :  # on teste si l'élément est présent dans la collection
    print('Présent')
else:
    print('Absent')

found = False   
for nom in noms :
    if nom == 'Jeanne':
        found = True
        break
if found :
    print('Présent')
else :
    print('Absent')  #! bloc équivalent à fonction 'in' précédente

print(sum(ages)) # pour additionner des valeurs numériques