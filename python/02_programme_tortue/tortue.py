import turtle

t = turtle.Turtle()

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)    

def spirale(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(45)
        t.forward(taille)
        t.left(45)
        t.forward(taille)
        t.left(45)
        taille += 5
    t.forward(taille)  

def carre(taille):
    for i in range(0, 4):
        t.back(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)

escalier(20, 5)

spirale(10, 10)

# carre(10)
# carre(30)
# carre(50)

carres(10, 10)

turtle.done()
