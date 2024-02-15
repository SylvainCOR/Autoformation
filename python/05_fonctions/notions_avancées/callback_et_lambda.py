# CALLBACK ET LAMBDA

# on stocke une fonction dans une variable

# principe de base :
def ma_fonction():
    print("toto")
    return 1

a = 5
b = ma_fonction   # sans les parenthèses !

print(f"A = {a} et B = {b()}")   # b() remplace ma_fonction()

# exemple sur les tables :
def mult_callback(a, b):
    return a*b

def add_callback(a, b):
    return a+b

def power_callback(a, b):
    return pow(a,b)

def afficher_table(n, opérateur_str, operation_cbk):
    for i in range (1, 11):
        print(f"{i} {opérateur_str} {n} = {operation_cbk(i, n)}")

afficher_table(2, "+", add_callback)
print()
afficher_table(3, "x", mult_callback)
print()
afficher_table(4, "^", power_callback) 
print()
# fonctions lambdas pour inclure le code directement à la place d'une fonctions classique :
afficher_table(5, "+", lambda a, b : a+b)
print()
afficher_table(6, "x", lambda a, b : a*b)
print()
afficher_table(7, "^", lambda a, b : pow(a,b))