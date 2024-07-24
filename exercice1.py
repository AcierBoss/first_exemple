# Question1

temps = 6.892
distance = 19.7
calcul_vitesse = distance / temps
calcul_vitesse = round(calcul_vitesse, 2)
print(f"La vitesse est: {calcul_vitesse} m/s")

                        #RETENONS
"""
Pour forcer un numbre de nombre apres la virgule apres le calcul d'une valeur de type float:
on utilise la fonction round('la valeur', 'nombre_voulu')
"""


# Question2
name = input("Veuillez entrer votre nom: ")
year = input("Veuillez entrer votre age: ")
try:
   year = float(year)
except ValueError:
    print("ERREUR: Vous devez entrer une valeur numerique")

print(f"Votre nom est: {name} et vous etes agés de: {year} ans")

