# Modificateurs d’accès : Public, private, protected
# Non définit explicitement dans python
""" 
Par convention on a :
    -> public :
        (valeur par défaut) 
        accès depuis l'intérieur et l'extérieur de la classe
    -> private : 
        __nom
        accès depuis l'intérieur de la classe uniquement
    -> protected :
        _nom
        accès depuis l'intérieur de la classe et des classes dérivées """

class Personne:
    def __init__(self, nom):
        self._nom = nom

    def se_presenter(self):
        print(f"Je m'appelle {self._nom}")

class Etudiant(Personne):
    def se_presenter(self):
        print(f"Je suis étudiant, je m'appelle {self._nom}")


#----Private----
personne1 = Personne("Jean")
# personne1.__nom = "Toto" # la variable nom n'est pas altérée
personne1.se_presenter() 
# print(personne1.__dict__) # en réalité une 2eme variable est créée

#----Protected----
personne2 = Etudiant("Tom")
# personne2._nom = "Toto" # la variable peut être altérée
personne2.se_presenter()
print(personne2.__dict__)