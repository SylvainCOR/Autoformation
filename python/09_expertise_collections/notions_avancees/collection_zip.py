pizzas_nom = ("4 formages", "Reine", "Calzone")
pizzas_prix = (10.5, 9, 12)

nom_et_prix = list(zip(pizzas_nom, pizzas_prix))
print(nom_et_prix)

for (nom, prix) in zip(pizzas_nom, pizzas_prix) :
    print(f"{nom} - {prix}€")

noms, prix = zip(*nom_et_prix)
print(noms, prix)