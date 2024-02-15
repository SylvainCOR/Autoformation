# Inverser une chaine de caractères

exemple = "Bonjour Toto"
print(exemple)

# avec fonction/boucle
def inverse(chaine) :
    resultat = ""
    for i in range(len(chaine)) :
        resultat = chaine[i] + resultat
    return resultat

print(inverse(exemple))

# avec un slice
print(exemple[::-1])

