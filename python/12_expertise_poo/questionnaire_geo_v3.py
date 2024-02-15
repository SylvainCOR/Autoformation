# Pratiquer sur la POO
# Mener un raisonnement sur du code existant
""" 
-> Définir les entités :
      Question
          - titre           - str
          - choix           - (str)
          - bonne_reponse   - str

          - poser()         -> bool

      Questionnaire
          - questions       - (Question)

          - lancer()
 """

class Question :

    def __init__(self, titre, choix, reponse):
        self.titre = titre
        self.choix = choix
        self.reponse = reponse

    def poser(self, numero):
        print(f"\nQUESTION n°{numero}:")
        print("\t" + self.titre)
        for i in range(len(self.choix)) :
            print(f"\t\t{i+1}) {self.choix[i]}")
        print()
        reponse_int = Question.demander_reponse(1, len(self.choix))
        if self.choix[reponse_int-1] == self.reponse :
            print("Bonne réponse !")
            return True
        else :
            print("Mauvaise réponse !")
        return False  

    def demander_reponse(min, max):
        reponse_str = input(f"Votre réponse (entre {min} et {max}): ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max :
                return reponse_int
            print(f"ERREUR : la valeur doit être comprise entre {min} et {max}")
        except:
            print("ERREUR : entrez une valeur numérique")
        return Question.demander_reponse(min, max)

class Questionnaire :

    def __init__(self, questions):
        self.questions = questions
    
    def lancer(self):
        score = 0
        for i, question in enumerate(self.questions, start=1) :
            if question.poser(i):
                score += 1
        print(f"\nVotre score est de : {score} sur {len(self.questions)}\n")
        return score

 
questionnaire = Questionnaire(
    (
    Question("Quelle est la capitale du Zimbabwe ?", ("Lusaka", "Kinshasa", "Harare", "Lilongwe", "Maputo"), "Harare"),
    Question("Quel pays n'est pas une ile ?", ("Hong-Kong", "Singapour", "Sri-Lanka"), "Hong-Kong"),
    Question("Quel état n'appartient pas au Canada ?", ("Nouvelle-Écosse", "Québec", "Territoires du Nord-Ouest", "Dakota du Nord"), "Dakota du Nord"),
    Question("Quelle mer se situe sous l'équateur ?", ("Mer du Labrador", "Mer de Béring", "Mer de Corail", "Mer des Caraïbes"), "Mer de Corail")
    )
).lancer()

