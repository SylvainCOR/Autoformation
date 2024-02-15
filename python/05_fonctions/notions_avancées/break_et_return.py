# DIFFÉRENCE ENTRE BREAK ET RETURN

# break : pour casser une boucle / dans une fonction ou dans le programme principal / ne prends pas de valeur
# return : pour sortir de la fonction / spécifique aux fonctions / peut prendre une valeur

# exemple :
def a():
    print("début")
    for i in range(0,25):
        if i > 20 :
            break   # return ne permettrait pas d'afficher la suite de la fonction -> print("fin")
        print(i)
    print("fin")

a()