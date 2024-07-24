
def Compter_Voyelle(chaine):
    voyelles = "aeiouyAEIOUY"
    compter = 0
    for lettre in voyelles:
        if lettre in chaine:
            compter += 1
            
    return compter


def contient_valeur_numerique(chaine):
    verification = any([element.isdigit() for element in chaine])
    return verification


while True:
    choix = input("Voulez vous introduire une autre phrase ? (y or n) : ")
    if choix == "y":
        listes = []
        phrase = input("Incrivez la phrase dont vous voulez compter le nombre de voyelle ? : ")
        if phrase == "":
            print("ERREUR: La phrase est vide, veuillez introduire une phrase")
        elif contient_valeur_numerique(phrase):
            print("ERREUR: La phrase ne doit pas contenir des chiffres")
        else:
            listes.append(phrase)
            nombre_voyelle = Compter_Voyelle(phrase)

            print(f"La phrase '{phrase}' contient '{nombre_voyelle}' voyelles")
    if choix == "n":
        print("AU REVOIR ! A bientot ")
        break
    if not choix == "y" or choix == "n":
        print("ERREUR: Vous devez entrer y ou n")
        