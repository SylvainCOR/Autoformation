

def afficher_table_multiplication(n, min=1, max=10):
    if min > max :
        print("ERREUR : Le MIN ne peut pas être supérieur au MAX !")
        return
    for i in range(min, max+1):
        print(f"{i} x {n} = {i*n}")


n = int(input("Quelle table souhaitez-vous afficher ? "))

afficher_table_multiplication(n)