
# def pizza_existe(e, collection) :
#     for i in collection :
#         if i == e :
#             return True
#     return False

def ajouter_pizza_utilisateur(collection) :
    pizz = input("Ajouter une pizza : ")
    # if pizza_existe(pizz, collection):
    if pizz.lower() in collection :
        print("Erreur : la pizza existe déjà")
    else :
        collection.append(pizz)

def tri_perso(e) :
    return len(e)

def afficher(collection, nb = -1) :
    c = collection
    if nb != -1 :
        c = collection[:nb]

    print(f"---------- LISTE DES PIZZAS ({len(c)}) ----------")
    collection.sort(reverse = True, key = tri_perso)
    print()
    if len(c) == 0 :
        print("AUCUNE PIZZA")
        return
    for i in c :
        print(i)
    print()
    print(f"Première pizza : {c[0]}")
    print(f"Dernière pizza : {c[-1]}")



pizzas = ["margherita", "4 fromages", "saumon", "calzone", "texane"]
vide = ()

# ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)
