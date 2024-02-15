# EXECRCICES COLLESTIONS : LISTES / TUPLES

#-------------------------------
# In insensible à la casse

def element_dans_la_liste(e, l):
    # for el in l :
    #     if e.lower() == el.lower() :
    #         return True
    # return False
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower

#          0        1         2          3          4       5
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé', 'Martin']

if element_dans_la_liste("jean", noms) :
    print("Elément trouvé")
else :
    print("Elément non trouvé")

print()
#-------------------------------
# Extraire les extensions (mon code)

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definitions_extensions = (("doc", "Document Word"),
                          ("exe", "Executable"),
                          ("txt", "Document texte"),
                          ("jpeg", "Image JPEG"))

def separation_extension(liste):    # récupérer liste d'extensions
    return [f.split(".")[-1] if "." in f else "" for f in liste]

def slice_definitions_extensions(liste) :
    ext = []
    for i in range(len(liste)) :
        e = liste[i][0]
        ext.append(e)
    return ext

def retourner_type_fichier(liste1, liste2) :
    if element_cherche == "" :
        return "Aucune extension"
    elif element_cherche in liste1 :
        e_index = liste1.index(element_cherche)
        return liste2[e_index][1]
    else :
        return "Extension non connue"

extension = separation_extension(fichiers)
ext_slice = slice_definitions_extensions(definitions_extensions)

for i in range(len(extension)) :
    element_cherche = extension[i].lower()
    type_fichier = retourner_type_fichier(ext_slice, definitions_extensions)
    print(f"{fichiers[i]} ({type_fichier})")

print()
#-------------------------------
# Extraire les extensions (correction)

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definitions_extensions = (("doc", "Document Word"),
                          ("exe", "Executable"),
                          ("txt", "Document texte"),
                          ("jpeg", "Image JPEG"))

def extraire_extension(nom_fichier) :
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) > 1 :
        return nom_fichier_split[-1]
    return None

def obtenir_definition_extension(extensions, definitions) :
    for d in definitions :
        if d[0].lower() == extensions.lower() :
            return d[1]
    return None

for fichier in fichiers :
    ext = extraire_extension(fichier)
    if ext :
        definition = obtenir_definition_extension(ext, definitions_extensions)
        if not definition :
            definition = "Extension non connue"
    else :
        definition = "Aucune extension"
    print(fichier + " (" + definition + ")")

print()
#-------------------------------
# Nombre total de carcatères

#          0        1         2          3          4       5
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoé', 'Martin']

# méthode 1 - for / len 
nb = 0
for nom in noms :
    nb += len(nom)
print("1- Nombre total de carcatères :", nb)

# méthode 2 - completion de liste / sum
longueur_noms = [len(nom) for nom in noms]
print("2- Nombre total de carcatères :", sum(longueur_noms))

# méthode 3 - join / len
print("3- Nombre total de carcatères :", len("".join(noms)))