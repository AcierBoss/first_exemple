import time

# C'est un programme de cuisson d'oeufs
print("Bienvenu sur notre programme de cuisson d'oeuf\n")
print("Ce programme permet de montrer le temps réel de cuissons de l'oeuf")
print("a- Oeufs à la coque (3min)")
print("b-Oeufs mollets (6min)")
print("c-Oeufs durs (9min)")

while True:
    choix = input("Entrer votre choix entre (a, b ou c) : ")
    if  choix == "a" or choix == "b" or choix == "c":
        break
    else:
        print("ERROR: Veuillez entrer un choix entre (a, b ou c) \n")
    
if choix == "a":
    duree = 3 * 60
    
if choix == "b":
    duree = 6 * 60
    
if choix == "c":
    duree = 9 * 60
    
print("Cuisson en cours", end="", flush= True)
while True:
    for i in range(10):
        duree -=1
        time.sleep(1)
        print(".", end="", flush= True)
    if duree <= 0: # Condition permettant de sortir de la boucle si la durée 
        break
    print("")
    min = duree // 60
    sec = duree - min * 60
    print(f"La durée restante est de {min:02d}:{sec:02d}", end="", flush= True) # Afficher lenombre de min et de seconde restante

print()
print("FELICITATION: Cuisson terminée")
