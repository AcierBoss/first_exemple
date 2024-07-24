class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
    
    
    def Afiicher(self):
        veg_str = "-Pizza Non Végétarienne"
        if self.vegetarienne:
            veg_str = " -Pizza Végétarienne"
        print(f"Nom de la Pizza: {self.nom}")
        print(f"Prix de la Pizza: {self.prix}£")
        print("Végétarienne: " + veg_str)
        print("Ingrédients:", ", ".join(self.ingredients))
        
        
        
pizzas = [
            Pizza("Margheritha", 7.99, ("tomate", "mozzarrella", "basilic", "huile d'olive"))
          
          ]
for i in pizzas:
    i.Afiicher()