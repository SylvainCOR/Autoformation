# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur

        statut = "majeur" if self.EstMajeur() else "mineur"
        genre = " homme" if self.genre else "e femme"
        e_option = "" if self.genre else "e"

        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        print("Je suis un" + genre)
        print("Je suis " + statut + e_option)
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 30, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()