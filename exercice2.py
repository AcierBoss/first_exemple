"""#Question1

liste = [17, 38, 10, 25, 72]
liste.sort()                #  Trier la liste et afficher
print(liste)
liste.append(12)            # Ajouter 12 à la liste et afficher
print(liste)
liste.reverse()             # Inverser les éléments de la liste et afficher
print(liste)
print(liste.index(17))      # Afficher l'indice du numéro 17
liste.remove(38)            # Supprimer 38 de la liste et afficher
print(liste)
print(liste[1:3])           # Afficher la sous liste du 2è au 3è élément
print(liste[:2])            # Afficher la sous liste du 2è élément
print(liste[2:])            # Afficher la sous liste du 2è au 3è élément
print(liste[:])             # Afficher la sous liste du 3è élément à la fin
print(liste[-1])            # Afficher la sous liste complète de la liste
"""

# Question2

truc =[]
machin = [0.0]*5
print("Le truc:", truc)
print("Le machin:", machin)
for i in range(4):
    print(i, end=" ")
print()
    
for entier in range(4, 8):
    print(entier, end=" ")
print()
    
for entiers in range(2, 9, 2): #   La fonction range() prend en pararamètre une valeur initiale, une valeur finale, et éentuellement              #
    print(entiers, end=" ")             #    le nombre de rebonds qu'on désir effectuer
print()

chose = [0, 1, 2, 3, 4, 5]

if 3 in chose:
    print("La valeur 3 est trouvée")
elif 6 in chose:
    print("La valeur 6 est trouvée")
else:
    print("La valeur recherchée n'est pas trouvée")
    
# Question3
liste1 = []
for i in range(6):
    liste1.append(i+3)
print(liste1)

# Question4
liste2 = []
for i in range(6):
    if i >= 2:
        liste2.append(i+3)
print(liste2)

# Question5

chaine = []
for i in "abc":
    for e in "de":
        chaine.append(i+e)
print(chaine)

# Question6
somme = 0
for i in range(10):
    somme += i
print("La somme des chiffres est:", somme)