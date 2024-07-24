import time

print("Ce programme permet de suivre en temps réel la cuisson de vos oeufs.")
print("a- Oeufs moelles")
print("b- Oeufs dur")
print("c- Oeufs solide")
print("d- Oeufs naturel")

while True:
    choix = input("Quel type de cuisson voulez vous faire ? : ")
    if choix == "a" or choix == "b" or choix == "c" or choix == "d": # Gérer les cas d'erreur
        break
    print("ERREUR: Vous devez faire un choix entre (a, b, c ou d)\n")

if choix == "a":
    print("GREAT: C'est parti pour une cuisson de 3min\n")
    duree = 3 * 60
if choix == "b":
    print("GREAT: C'est parti pour une cuisson de 6min")
    duree = 6 * 60
if choix == "c":
    print("GREAT: C'est parti pour une cuisson de 9min")
    duree = 9 * 60
if choix == "d":
    print("GREAT: C'est parti pour une cuisson de 12min")
    duree = 12 * 60

print("Cuisson en cours", end="", flush= True)    
while True:
    for i in range(10):
        duree -= 1
        time.sleep(1) # Permet d'arreter le temps pendant 1s
        print(".", end="", flush= True)
    if duree <= 0:
        break

    minutes = duree // 60
    secondes = duree - minutes * 60
    print()
    print(f"La durée restante est de {minutes:02d}:{secondes:02d}", end="", flush= True) # Afficher le temps restant apres 10s

print()
print("CONGRAGULATION: Cuisson terminée")
