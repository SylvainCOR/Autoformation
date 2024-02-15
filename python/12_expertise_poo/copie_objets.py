import copy
# COPIER DES OBJETS
# shallow copy / deep copy

class Personne:
    def __init__(self, nom, age, amis):
        self.nom = nom
        self.age = age
        self.amis = amis

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")
        print("Amis : " + str(self.amis))


#-----SHALLOW COPY-----
personne1 = Personne("Jean", 20, ["Claire", "Marc", "Emilie"])
personne2 = copy.copy(personne1) # crée un 2eme objet (copie peu profonde)

personne1.nom = "Toto" # n'altère pas personne2
personne1.amis[0] = "Chantale" # altètre la liste de personne2

personne1.AfficherInfos()
personne2.AfficherInfos()
print()

#-----DEEP COPY-----
personne3 = copy.deepcopy(personne2) # copie profonde
personne2.amis[0] = "Marc"# n'altère pas personne3

personne2.AfficherInfos()
personne3.AfficherInfos()




