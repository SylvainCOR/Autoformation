

def poser_question(n, question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print(f"QUESTION N°{n} :")
    print("\t" + question)
    print("\t (a) " + r1)
    print("\t (b) " + r2)
    print("\t (c) " + r3)
    print("\t (d) " + r4)
    print()
    reponse = input("Votre réponse : ")

    if reponse != choix_bonne_reponse :
        print("Mauvaise réponse !")
    else :
        print("Bonne réponse !")
        score += 1
    print()    


score = 0

poser_question(1, "Quelle est la capitale du Zimbabwe ?", "Lusaka", "Harare", "Lilongwe", "Maputo","b")
poser_question(2, "Quel pays n'est pas une ile ?", "Hong-Kong", "Singapour", "Sri-Lanka", "Japon","a")
poser_question(3, "Quel état n'appartient pas au Canada ?", "Nouvelle-Écosse", "Québec", "Territoires du Nord-Ouest", "Dakota du Nord","d")
poser_question(4, "Quelle mer se situe sous l'équateur ?", "Mer du Labrador", "Mer de Béring", "Mer de Corail", "Mer des Caraïbes","c")

print("Votre score est de :", score, "sur 4")
