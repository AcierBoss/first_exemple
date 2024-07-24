import os
import random
import time


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


sequence = "" # Initialiser une séquence vide afin de stocker les chiffes aléatoires dedans
for chiffre in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre) # Stockage des chiffres dans la séquence sous forme d'une chaine de caractère
clear_screen() # Nettoyage de l'écran

score = 0 # Initialisation du score à 0 afin de l'incrémenter par la suite
while True:   # Boucle infinie tanque l'utilisateur entre la bonne séquence
    print("Retenez la séquence : ")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    user_answer = input("Entrer votre réponse : ") # Demander à l'utilisateur d'entrer sa réponse
    if user_answer == sequence:                    # Vérifier si la réponse de l'utilisateur est égale à la séquence
        print("Bonne réponse")                     # Afficher bonne réponse
        time.sleep(1)                              # Maintenir l'affichage pendant 1 seconde
        score += 1                                 # Incrémentation du score si l'etilisateur entre la bonne séquence
    else:
        break                                      # Condition de sortir de la boucle si la réponse est fause

    chiffre = random.randint(0, 9) # Afficher les chiffres initialement établi
    sequence += str(chiffre)   # Ajouter un nouveau chiffre aléatoire compris entre 0 et 9 aux chiffres précédent
    clear_screen()


print("Mauvaise réponse")
print(f"La  bonne séquence etait de : {sequence}")
print(f"Votre score est : {score}")


# Des conditions pour juste m'amuser
if score < 5:
    print("DECISION: Vous pouvez faire mieux")
elif 5 < score <= 10:
    print("DECISION: Vous etes vraiment à féliciter")
else:
    print("DECISION: Vous etes un génie")


# NB: Donc c'était tout ce que je voulais pour l'exercices. Des questions si vous n'avez pas compris.