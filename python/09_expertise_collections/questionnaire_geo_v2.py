
def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max :
            return reponse_int
        print(f"ERREUR : la valeur doit être comprise entre {min} et {max}")
    except:
        print("ERREUR : entrez une valeur numérique")
    return demander_reponse_numerique_utilisateur(min, max)

def poser_question(question):
    choix = question[1]
    print()
    print("QUESTION :")
    print("   " + question[0])
    for i in range(len(choix)) :
        print(f"      {i+1}) {choix[i]}")

    print()
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))

    if choix[reponse_int-1].lower() == question[2].lower() :
        print("Bonne réponse !")
        return True
    else :
        print("Mauvaise réponse !")
    return False  


'''
    questionnaire    
        question
            titre = "Quelle est la capitale du Zimbabwe ?"
            reponses = ("Lusaka", "Harare", "Lilongwe", "Maputo")
            bonne_reponse = "Harare"
'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire :
        if poser_question(question):
            score += 1
    print()
    print(f"Votre score est de : {score} sur {len(questionnaire)}")


questionnaire = (
    ("Quelle est la capitale du Zimbabwe ?", ("Lusaka", "Harare", "Lilongwe", "Maputo"), "Harare"),
    ("Quel pays n'est pas une ile ?", ("Hong-Kong", "Singapour", "Sri-Lanka", "Japon"), "Hong-Kong"),
    ("Quel état n'appartient pas au Canada ?", ("Nouvelle-Écosse", "Québec", "Territoires du Nord-Ouest", "Dakota du Nord"), "Dakota du Nord"),
    ("Quelle mer se situe sous l'équateur ?", ("Mer du Labrador", "Mer de Béring", "Mer de Corail", "Mer des Caraïbes"), "Mer de Corail")
)

lancer_questionnaire(questionnaire)