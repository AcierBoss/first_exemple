nom = input("Quel est votre nom ? :")
while not nom.strip():
    print("Le nom ne peut être vide")
    nom = input("Quel est votre nom ? :")
    print("Bonjour,", nom)

annee = input("Entrez votre annee de naissance:")
annee = int(annee)
anneeactuel= 2024
while True:
    if annee < anneeactuel:
        break
    else:
        print("L'année de naissance doit être inferieur à l'annee actuelle.")
        age = anneeactuel - annee

        print(f"salut{nom}! vous avez {age} ")
if age >= 18:
    print("vous etes majeur(e)")
else:
    print("vous etes mineur(e)")

