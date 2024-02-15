# FONCTION RÉCURSIVES : on rappelle une fonction dans cette fonction

# application numérique :
def a(n, limite):
    if n > limite :
        return
    print(f"résultat = {n}")
    a(n*n, limite)

a(2, 100000)

# traitement de données :
def choix_utilisateur(min, max):
    reponse_str = input(f"Quel est votre choix entre {min} et {max} ? ")
    try :
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max :
            print("Réessayez entre les limites")
            return choix_utilisateur(min, max)
        return reponse_int
    except :
        print("Il faut entrer un nombre")
        return choix_utilisateur(min, max)

choix = choix_utilisateur(5, 25)
print("choix = " + str(choix))
