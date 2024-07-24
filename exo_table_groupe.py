def afficher_infos_table_multiplication(nombre):
    while True:
        min_str = input("Entrer le plus petit nombre de la table : ")
        max_str = input("Entrer le plus grand nombre de la table : ")
    
        try:
            min_int = int(min_str)
            max_int = int(max_str)

        except ValueError:
            print("ERREUR: Le nombre min ou max ne doit pas contenir des caractères")
        else:
            if max_int < min_int:
                print("ERREUR: Le nombre minimum ne doit pas etre inférieur au nombre maximun")
            else:
                for i in range(min_int, max_int):
                    produit = nombre * i
                    print(f"{nombre} x {i} = {produit}")
                break   

while True:
    user_number_str = input("Entrer le nombre dont vous voulez la table de multiplication : ")
    try:
        user_number_int = int(user_number_str)
    except ValueError:
        print("ERREUR: Vous devez entrer un nombre entier !")
    else: 
         break

afficher_infos_table_multiplication(user_number_int)