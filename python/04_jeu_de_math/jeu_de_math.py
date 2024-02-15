import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0,1)
    operateur_str = "+"
    if o == 1 :
        operateur_str = "*"
    reponse_str = input(f"Calculez : {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a + b
    if o == 1 :
        calcul = a * b
    if reponse_int == calcul :    
        return True
    return False
    
nb_points = 0

for i in range(0, NB_QUESTIONS):
    print(f"Ceci est la question n°{i+1} sur {NB_QUESTIONS}")

    if poser_question() == True :
        print("Résultat correct !")
        nb_points += 1
    else :
        print("Résultat incorrect !")
    print()

print(f"Votre résultat est : {nb_points} / {NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS :
    print("Bien joué !")
elif nb_points == 0 :
    print("Aucune réponse correcte...")
elif nb_points > moyenne :
    print("Pas mal !!")
else :
    print("Peut mieux faire !")
print()

