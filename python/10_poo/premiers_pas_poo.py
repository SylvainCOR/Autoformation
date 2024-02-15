# - Différences programmation impérative / objet
# - Le plus simple possible
# - Exercices, mises en situation

#-----PROGRAMMATION IMPERATIVE-----

def afficher_info_personne(nom, age):
    print(f"La personne s'appelle {nom}, son age est de {age} ans.")

def demander_nom_personne():
    return input("Quel est votre nom ? ")

nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

# afficher_info_personne(nom1, age1)
# afficher_info_personne(nom2, age2)

# nom3 = demander_nom_personne()
age3 = 18
# afficher_info_personne(nom3, age3)


#-----DEFINITION POO-----

""" 
    Personnes, entité : classe
    Données : nom, age
    Actions : méthodes()
        - SePresenter()
        - DemanderNom() / input


      EtreVivant                  Classe parent
  Chat        Personne            Classes enfants (ou classes dérivées) """

class EtreVivant : 
    ESPECE_ETRE_VIVANT = "non identifié"

    def AfficherInfoEtreVivant(self): 
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)


class Chat(EtreVivant): # heritage de la fonction
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"


class Personne(EtreVivant) : # crée une classe d'objet
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo Sapiens)"  # crée une variable de classe (1 pour toutes les personnes)

    def __init__(self, nom: str = "", age: int = 0): # crée un constructeur (conventionnellement __init__)
        self.nom = nom  # crée une variable d'instance
        self.age = age
        if nom == "" :
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):  # crée une méthode (= fonction dans une classe)
        info_personne = f"Bonjour, je m'appelle {self.nom} !"
        if self.age == 0 :
            print(info_personne)
        else :
            if self.EstMajeur() :
                statut = "majeur"
            else :
                statut = "mineur"
            print(f"{info_personne} J'ai {self.age} ans et je suis {statut}.")

    def EstMajeur(self):    # crée une autre méthode
        return self.age >= 18 

    def DemanderNom(self):
        self.nom = input("Quel est votre nom ? ")

""" 
    # cas n°1 (pour appeler une variable de classe)
    def AfficherInfoEtreVivant():   # crée une méthode de classe
        print("Info être vivant : " + Personne().ESPECE_ETRE_VIVANT)

    # cas n°2 (en utilisant le self car variable commune à tous les objets)
    def AfficherInfoEtreVivant(self): 
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT) """


#-----UTILISATION-----
print()

liste_personnes = [Personne("Jean", 30), 
                   Personne("Paul", 15),
                   Personne("Zoé", 20)]
print()

for personne in liste_personnes :
    personne.SePresenter()
    personne.AfficherInfoEtreVivant()
""" 
    Personne().AfficherInfoEtreVivant()   # cas n°1 (ne dépend pas de l'instance)
    personne.AfficherInfoEtreVivant()   # cas n°2  """

print()
chat = Chat()
chat.AfficherInfoEtreVivant()
etrevivant = EtreVivant()
etrevivant.AfficherInfoEtreVivant()
