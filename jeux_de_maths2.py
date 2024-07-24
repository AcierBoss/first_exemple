import random


NOMBRE_MIN = 0
NOMBRE_MAX = 100
NOMBRE_QUESTIONS = 10


def poser_question():
    nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    valeur = random.randint(0, 3)
    
    operateur_str = "+"
    if valeur == 1:
        operateur_str = "*"
    if valeur == 2:
        operateur_str = "-"
        
    print(f"Calculez {nombre1} {operateur_str} {nombre2}")
    reponse_str = input("Quel est votre réponse ?: ")
    try:
        reponse_int = int(reponse_str)
    except:
        print("ERREUR: Vous devez entrer un nombre entier\n")
        return poser_question()
    
    calcul = nombre1 + nombre2
    if valeur == 1:
        calcul = nombre1 * nombre2
    if valeur == 2:
        calcul = nombre1 - nombre2
    if reponse_int == calcul:
        return True
    return False


print("Bienvenu sur ce programme vous permettant de faire le calcul de 10 questions pris de façon aléatoire\n")


score = 0
for i in range(0, NOMBRE_QUESTIONS):
    print(f"Question n°{i + 1} sur {NOMBRE_QUESTIONS}")
    if poser_question():
        print("Réponse correcte\n")
        score += 1
    else:
        print("Mauvaise réponse\n")

print(f"Votre score finale est de {score} sur {NOMBRE_QUESTIONS}")
    
    
    