"""
0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.
1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence
2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde
3 - Afficher la séquence à mémoriser pendant 3 secondes
4 - Nettoyer l'écran et demander la réponse à l'utilisateur
5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1
6 - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"
"""

import os
import time
import random


def clear_screen(): # Cette fonction permet de nettoyer le contenu de l'écran
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        

sequence = ""
for chiffre in range(4): # initialiser la séquence à retenir à 4 chiffres
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)
clear_screen()
print("Welcome in the Simon game\n")

score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1) # Afficher "Retenez la séquence" pendant 1 seconde
    print(sequence)
    time.sleep(3) # Afficher la séquence à retenir pendant 3s
    clear_screen()
    
    user_answer = input("Veuillez entrer votre réponse : ")
    if user_answer == sequence:
        print("Bonne réponse")
        score +=1 # Incrémentation du score en cas de bonne réponse
        print(f"Votre score est de :{score}")
        time.sleep(1)
       
    else:
        break
    
    chiffre = random.randint(0, 9) # Afficher les quatre chiffres initiales entre 0 et 9 de façon aléatoire 
    sequence += str(chiffre) # Ajout d'un nouveau chiffre aléatoire à la séquence
    clear_screen()
    

print("Mauvaise reponse")
print(f"La séquence était {sequence}")
print(f"Votre score finale est : {score}")

if score < 5:
    print("DECISION: Vous pouvez faire mieux")
elif 5 < score <= 10:
    print("DECISION: Vous etes vraiment à féliciter")
else:
    print("DECISION: Vous etes un génie")