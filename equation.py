from math import sqrt


def resolution_equation_lineaire(a, b):
    if a == 0:
        if b == 0:
            return "Tous les nombres sont des solutions"
        else:
            return "L'équation n'admet pas de solution"
    else:
        return -b / a
    

def resolution_equation_quadratique(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        resultat1 = (-b - sqrt(delta))/ (2 * a)
        resultat2 = (-b + sqrt(delta))/ (2 * a)
        print(f"L'équation admet deux solutions distinctes : {variable}1 = {resultat1} et {variable}2 = {resultat2}")
    elif delta < 0:
        print("L'équation n'adamet pas de solution dans réelle")
    else:
        resultat = -b /( 2 * a)
        print(f"L'équation admet une solution réelle: {variable} = {resultat}")

def resolution_equation(a, b, c=0):
    if a == 0:
        resultat = print("La résolution de cette équation de 1er degré est :", resolution_equation_lineaire(b, c))
        return resultat
    else:
        return resolution_equation_quadratique(a, b, c)
    
  
    

# Programme principale

while True:
    variable = input("Quel est la variable de votre équation ? : ")
    if len(variable) > 1:
        print("ERREUR: La variable de votre équation doit etre une lettre. Ex: x, y, t...\n")
    elif variable == int(variable):
         print("ERREUR: La variable de votre équation ne doit pas etre un chiffre.\n")
    else:
        break
   
while True:
    coefficient1_str = input("Entrer le premier coef : ")
    coefficient2_str = input("Entrer le deuxième coef : ")
    coefficient3_str = input("Entrer le troisième coef : ")

    try:
        coefficient1_float = float(coefficient1_str)
        coefficient2_float = float(coefficient2_str)
        coefficient3_float = float(coefficient3_str)
    except:
        print("ERREUR: Vous devez entrer un entier pour les coefficients \n")
    else:
        break

resolution_equation(coefficient1_float, coefficient2_float,coefficient3_float)