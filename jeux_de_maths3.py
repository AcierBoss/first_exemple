import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_DE_QUESTION = 2


def ask_question():
    number1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    number2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    valor = random.randint(0, 4)

    operateur_str = "+"
    if valor == 1:
        operateur_str = "*"
    if valor == 2:
        operateur_str = "/"
    if valor == 3:
        operateur_str = "-"

    print(f"Calculez : {number1} {operateur_str} {number2}")

    calcul = number1 + number2
    if valor == 1:
        calcul = number1 * number2
    if valor == 2:
        calcul = number1 / number2
    if valor == 3:
        calcul = number1 - number2

    user_answer_str = input("Votre réponse : ")

    try:
        user_answer_float = float(user_answer_str)
        user_answer_float = round(user_answer_float, 2)
    except:
        print("ERROR: Enter an interger number")
    else:
        if user_answer_float == calcul:
            return True
        False

# Menu
print("")
print("******************** Bienvenu dans le projet... JEUX DE MATHS ! ********************** \n")

print("Quel est votre niveau en mathématique ? ")
print("1- Débutant")
print("2- Moyen")
print("3- Dificile")
print("4- Expert")

while True:
    choice_str = input("Votre choix : ")
    try:
        choice_int = int(choice_str)
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre entier compris entre (1 et 4) \n")
    else:
        if choice_int == 1 or choice_int == 2 or choice_int == 3 or choice_int == 4:
            break
        else:
            print("ERREUR: Faites un choix entre (1, 2, 3 ou 4) \n")

if choice_int == 1:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 5
    NOMBRE_DE_QUESTION = 5
    score = 0
    for i in range(0, NOMBRE_DE_QUESTION):
        print(f"Question n°{i + 1} sur {NOMBRE_DE_QUESTION}")

        if ask_question():
            print("Bonne réponse \n")
            score += 1
        else:
            print("Mauvaise réponse \n")

    print(f"Votre score est: {score} sur {NOMBRE_DE_QUESTION}")

if choice_int == 2:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 10
    NOMBRE_DE_QUESTION = 10
    score = 0
    for i in range(0, NOMBRE_DE_QUESTION):
        print(f"Question n°{i + 1} sur {NOMBRE_DE_QUESTION}")

        if ask_question():
            print("Bonne réponse \n")
            score += 1
        else:
            print("Mauvaise réponse \n")

    print(f"Votre score est: {score} sur {NOMBRE_DE_QUESTION}")

if choice_int == 3:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 15
    NOMBRE_DE_QUESTION = 12 
    score = 0
    for i in range(0, NOMBRE_DE_QUESTION):
        print(f"Question n°{i + 1} sur {NOMBRE_DE_QUESTION}")

        if ask_question():
            print("Bonne réponse \n")
            score += 1
        else:
            print("Mauvaise réponse \n")

    print(f"Votre score est: {score} sur {NOMBRE_DE_QUESTION}")

if choice_int == 4:
    NOMBRE_MIN = 1
    NOMBRE_MAX = 20
    NOMBRE_DE_QUESTION = 20
    score = 0
    for i in range(0, NOMBRE_DE_QUESTION):
        print(f"Question n°{i + 1} sur {NOMBRE_DE_QUESTION}")

        if ask_question():
            print("Bonne réponse \n")
            score += 1
        else:
            print("Mauvaise réponse \n")

    print(f"Votre score est: {score} sur {NOMBRE_DE_QUESTION}")