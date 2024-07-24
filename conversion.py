def ask_conversion_user(unit1: str, unit2: str, factor: float):
    answer_str = input(f"Quel valeur en '{unit1}' voulez vous convertir en '{unit2}' (ou 'Enter' pour quitter) : ")
    if answer_str == "":
        return True # On peut mettre la foction exit() pour ssortir du programme
    try:
        answer_float = float(answer_str)
    except ValueError:
        print("ERREUR: Vous devez entrer un nombre entier ou à virgule")
        print("Svp utiliser point '.' en lieu et place de virgule ','\n")
        return ask_conversion_user(unit1, unit2, factor)
    
    calcul = round(answer_float * factor, 2)
    print(f"La conversion de {answer_float} {unit1} en {unit2} est : {calcul} {unit2}")
    return False


while True:
    print("Mon programme de conversion des unités")
    print("A- Convertion de POUCE en CENTIMETRE ")
    print("B- Convertion de CENTIMETRE en POUCE ")
    choose_str = input("Quel est votre choix ? : ")
    if choose_str == "A" or choose_str == "B":
        break
    print("ERREUR: Vous devez faire un choix entre (A et B)\n")
    
while True:
    if choose_str == "A":
        if ask_conversion_user("pouces", "cm", 2.54):
            break # Pas besoin de cette ligne si on utilisait la foction exit() in peut plus haut mais on doit use if
    if choose_str == "B":
        if ask_conversion_user("cm", "pouces", 0.394):
            break # Pas besoin de cette ligne si on utilisait la foction exit() in peut plus haut mais on doit use if
        