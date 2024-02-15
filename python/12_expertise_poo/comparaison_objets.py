# Comparer des objets
# is / ==

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age


personne1 = Personne("Jean", 20)
personne1.AfficherInfos()
personne2 = Personne("Jean", 20)
personne2.AfficherInfos()

print(personne1 == personne2)
# True avec la fonction d'égalité __eq__ sinon False
print(personne1 is personne2) 
# False car différentes instances
print(personne1.__dict__ == personne2.__dict__)
# compare les dictionnaires (cas où le code est inaccessible)