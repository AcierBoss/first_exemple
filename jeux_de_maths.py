import random


NOMBRE_MIN = 1
NOMBRE_MAX = 20
NOMBRE_QUESTION = 10

"""
Définir une fonction qui permet de demander à l'utilisateur une réponse au calcul. Elle gère le cas des erreurs, 
verifie les réponse et retourne si la réponse est vraie ou fausse
"""
def poser_question():
    nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX) # Nombre choisir de façon aléatoire
    nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    valeur = random.randint(0, 4)
    operateur_str ="+"
    if valeur == 1:
        operateur_str = "*"
    if valeur == 2:
        operateur_str = "/"
    if valeur == 3:
        operateur_str = "-"
    print(f"Calculez : {nombre1} {operateur_str} {nombre2}")
    reponse_str = input(f"Entrer votre réponse : ")
    try:
        reponse_float = float(reponse_str)
        reponse_float = round(reponse_float, 2)
    except:
        print("ERREUR: Veuillez entrer un nombre entier\n")
        return poser_question()
    
    calcul = nombre1 + nombre2
    if valeur == 1:
        calcul = nombre1 * nombre2
    if valeur == 2:
        calcul = nombre1 / nombre2
    if valeur == 3:
        calcul = nombre1 - nombre2
    
    if reponse_float == calcul:
        return True
    return False
    

    
"""
Boucle permettant le niméro de question sur le nombre de question total, icrémente le score si le résulat est juste
"""
score = 0
for i in range(0, NOMBRE_QUESTION):
    print(f"Question n°{i + 1} sur {NOMBRE_QUESTION}")
    if poser_question():
        print("Bonne réponse\n")
        score += 1
    else:
        print("Mauvaise réponse\n")
    
print(f"Votre score final est {score} sur {NOMBRE_QUESTION}")

# Des conditions pour apprécier l'utilisateur en fonction de son score
if score == NOMBRE_QUESTION:
    print("EXELLENT: Vous avez tous validé")
elif  5 <= score <= 9:
    print("GENIAL: Vous etes cultivez")
else:
    print("SORRY: Allez réviser vos cours de maths !")