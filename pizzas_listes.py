def afficher_pizzas(collection, n_premier_element = -2):
    c = collection
    if not n_premier_element == -2:
        c = collection[: n_premier_element]
    nombre_pizza = len(c)
    
    print(f"##########################----LISTES DE PIZZAS({nombre_pizza})----################################")
    
    if nombre_pizza == 0:
        print("Aucune pizza n'est disponible")
    else:
        for i in c:
            print(i)
        print()
        print("Le premier pizza est : ", c[0])
        print("Le dernier pizza est : ", c[-1])
        
        
def ask_pizza_user(collection):
    pizza_user = input("Veuillez ajouter une pizza : ")
    if pizza_user.lower() in collection:
        print("ERREUR: Cette pizza existe déjà !")
    else:
        collection.append(pizza_user)
        
            
        
pizzas = ["4 frommage", "Végétarienne", "hawai", "calzone"]

ask_pizza_user(pizzas)
print()
afficher_pizzas(pizzas, -2)