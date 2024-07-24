# Un programme python de conversion d'argent

def ask_coversion_user(unit1: str, unit2: str, factor: bool):
    user_answer_str = input(f"Combien de {unit1} voulez vous convertir  en {unit2} ou taper 'q' pour quitter : ")
    if user_answer_str == "q":
        return True
    try:
        user_answer_float = float(user_answer_str)
    except ValueError:
        print("ERREUR: Vous devez entrer un entier ou un nombre à virgule")
        print("SVP entrer un point '.' en lieu et place de virgule ',' MERCI !!!\n")
        return ask_coversion_user(unit1, unit2, factor)
    calcul = user_answer_float * factor
    calcul = round(calcul, 2)
    print(f"La conversion de {user_answer_float}{unit1} est : {calcul} {unit2}")
    return False


while True:
    print("Un programme de conversion d'argent")
    print("a- Conversion de Dollar($) en Franc(CFA)")
    print("b- Conversion de Franc(CFA) en Dollar($)")
    print("c- Conversion de Euro(€) en Franc(CFA)")
    print("d- Conversion de Franc(CFA) en Euro(€)")
    print("e- Conversion de Dollar($) en Euro(€)")
    print("f- Conversion de Euro(€) en Dollar($)")
    
    choice = input("Quel est votre choix entre (a, b, c, d, e ou f) ? : ")
    if choice == "a" or choice == "b" or choice == "c" or choice == "d" or choice == "e" or choice == "f":
        break
    print("ERREUR: vous devez faire un choix entre (a, b, c, d, e ou f)\n")
    print("")
    
while True:
    if choice == "a":
        if ask_coversion_user("$", "CFA", 599.022):
            break
    if choice == "b":
        if ask_coversion_user("CFA", "$", 0.0017):
            break
    if choice == "c":
        if ask_coversion_user("€", "CFA", 655.5912):
            break
    if choice == "d":
        if ask_coversion_user("CFA", "€", 0.0015):
            break
    if choice == "e":
        if ask_coversion_user("$", "€", 0.9137):
            break
    if choice == "f":
        if ask_coversion_user("€", "$", 1.0944):
            break