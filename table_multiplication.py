def afficher_table_multiplication(nombre):
    min_str = input("Entrer le plus petit nombre de votre table : ")
    max_str = input("Entrer le plus grand nombre de votre table : ")
    try:
        min_int = int(min_str)
        max_int = int(max_str)
    except:
        print("ERREUR: Vous devez entrer des entiers\n")
        return afficher_table_multiplication(nombre)
    if min_int > max_int:
        print("ERREUR: Le plus petit nombre doit forcément etre inférieur au plus gand nombre \n")
        return afficher_table_multiplication(nombre)
    for i in range(min_int, max_int):
        produit = nombre * i
        print(f"{nombre} x {i} = {produit}")
     
     
     
# Programme Principal
print( )
print("Blue Sociaty 'PYTHON', vous souhaite la bienvenue dans notre programme de multiplication")
print("ALLEZ C'EST PARTI...\n")   # The header
while True:
    nombre_str = input("Entrer le nombre dont vous voulez la table de multiplication : ")
    try:
        nombre_int = int(nombre_str)
    except:
        print("ERREUR: Vous devez entrer un nobre entier\n")
    else:
        break # Permet de sortir de la boucle et de continuer la suite de l'exécussion du programme
    
    
    
afficher_table_multiplication(nombre_int)