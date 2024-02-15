# Méthodes d’instance, de classe et statiques

class Personne:
    TYPE = "Humain" # variable de classe
    def __init__(self, nom):
        self.nom = nom

    # méthode d'instance (utilise self)
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - " + self.TYPE)

    # méthode statique
    @staticmethod
    def formater_chaine(a): # premier caractère en majuscule puis minuscules
        return a[0].upper() + a[1:].lower()

    # méthode de classe (très peu utilisé)
    @classmethod
    def methode_de_classe(cls):
        print("Méthode de classe : " + cls.TYPE)


personne1 = Personne("jean")
personne1.se_presenter()

print(Personne.formater_chaine("toTo"))
Personne.methode_de_classe()