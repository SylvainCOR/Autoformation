# nom, prix, ingredients, végétarienne

class Pizza :
    def __init__(self, nom, prix, ingredients, vege = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vege = vege
    
    def Afficher(self):
        veg = " - VEGETARIENNE" if self.vege else ""
        print(f"Pizza {self.nom} : {self.prix} €{veg}")
        print(", ".join(self.ingredients))
        print()

class PizzaPersonalisee (Pizza) :
    PRIX_DE_BASE = 8
    PRIX_PAR_INGREDIENT = 1.5
    dernier_numero = 0

    def __init__(self):
        PizzaPersonalisee.dernier_numero += 1
        self.numero = PizzaPersonalisee.dernier_numero
        super().__init__(f"Personalisée {self.numero}", 0, [])
        self.ajouter_ingredients()
        self.calculer_prix()
    
    def ajouter_ingredients(self) :
        print()
        print(f"Ingrédients pour la pizza numéro {self.numero} :")
        while True :
            ingredient = input("Ajoutez un ingredient (ou entrer pour terminer) : ")
            if ingredient == "" :
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_prix(self) :
        self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_PAR_INGREDIENT


print()
pizzas = [Pizza("4 Fromages", 13.50, ("mozzarella", "gorgonzola", "chèvre", "brie"), True)
        ,Pizza("Regina", 12.50, ("jambon", "champignons", "mozzarella"))
        ,Pizza("Saumon", 14.00, ("saumon fumé", "roquette", "ciboulette", "citron"))
        ,Pizza("Margherita", 9.50, ("tomates", "mozzarella"), True)
        ,Pizza("Saint-jacques", 16.50, ("noix de saint-jacques", "crevettes", "saumon fumé", "tomates fraîches", "mozzarella"))
        ,Pizza("Parme", 14.50, ("jambon de parme", "roquette", "tomates confites", "mozzarella"))
        ,Pizza("Veggie", 13.50, ("aubergines", "champignons", "poivrons", "artichauds", "tomates", "mozzarella"), True)
        # ,PizzaPersonalisee()
        # ,PizzaPersonalisee()
]

def tri(e):
    return len(e.ingredients)
pizzas.sort(key=tri)

for pizza in pizzas :
    if pizza.vege or "champignons" in pizza.ingredients :
        pizza.Afficher()
    # if not pizza.vege and pizza.prix > 14 : 
    #     pizza.Afficher()
    # pizza.Afficher()