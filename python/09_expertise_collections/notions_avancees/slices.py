#            0          1       2       3         4
noms = ['Christophe', 'Zoé', 'Jean', 'Sophie', 'Martin']

print(noms[:3]) # équivalent à  print(noms[0:3])

slices_noms = noms[::-2]
print(slices_noms)

slices_noms[0] = 'Toto'
print(slices_noms)

slices_noms = noms[-4:-1]
print(slices_noms)
print(noms[1:4])