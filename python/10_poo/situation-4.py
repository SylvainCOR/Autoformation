# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---

nb_personnes = 3
liste_personnes = []

for i in range(nb_personnes):
    nom = input(f"nom de la personne {i + 1} : ")
    liste_personnes.append(Personne(nom))

# liste_personnes = [<__main__.Personne object at 0x0000022B301BE2D0>, <__main__.Personne object at 0x0000022B301BE990>, <__main__.Personne object at 0x0000022B301BE9D0>]
# liste_personnes = [Personne("Titi"), Personne("Toto"), Personne("Tata")] 

for personne in liste_personnes:
    personne.SePresenter()

