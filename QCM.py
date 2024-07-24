# Mon programme de QCM

class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse
        
        
    # Methode permettant de demander une reponse entre le min et le max à l'utilisateur et gestion d'erreur    
    def demander_nombre_numerique_utilisateur(self, min, max):
        choix_str = input(f"Faites votre choix entre '{min}' et '{max}' : ")
        try:
            choix_int = int(choix_str)
            if min <= choix_int <= max:
                return choix_int
            print(f"ERREUR: Veuillez choisir entre {min} et {max}\n")
            return self.demander_nombre_numerique_utilisateur(min, max)
        except:
            print("ERREUR: Veuillez entrer un nombre entier\n")
            return self.demander_nombre_numerique_utilisateur(min, max)
        
        
    # Creation de la methode permettant de retourner si le résultat choisi est vrai ou faux    
    def poser(self): 
        reponse = self.choix
        bonne_reponse = self.bonne_reponse
        print("Question:")
        print("    ", self.titre)
        
        for i in range(len(reponse)): 
            nb = i + 1
            print("  ", nb, "-", reponse[i])
        print()
        reponse_question = False
        
        choix_int = self.demander_nombre_numerique_utilisateur(1, len(reponse))
        if reponse[choix_int - 1] == bonne_reponse:
            print("Bonne réponse")
            reponse_question = True
        else:
            print("Mauvaise réponse")
        print()
        return reponse_question
            
        
# Classe permettant d'incrémenter le score si la réponse est juste        
class Questionnaire:
     def __init__(self, questions):
         self.questions = questions
         
    
     def lancer(self):
         score = 0
         for question in questions:
             # print(f"Question: {len(question)} / {len(questions)}")
             if question.poser():
                 score += 1
         print(f"Votre score final est de : {score} / {len(self.questions)}\n")
            
        
        
        
        
questions = (
Question("Quel est le plus grand Océan du monde ?", ("L'océan Atlantique", "L'océan Indien", "L'océan pacifique"),"L'océan Atlantique"),
Question("Qui a écrit Roméo et Juliette ?", ("William Shakespeare", "Victor Hugo", "Molière"), "William Shakespeare"),
Question("Quelle est la capitalede l'Italie ?", ("Madrid", "Rome", "Paris"), "Rome"),
Question("Qui a peint 'La Joconde' ?", ("Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"), "Leonardo da Vinci"),
Question("Quel est le plus long fleuve du monde ?", ("Le Nil", "L'Amazone", "Le Mississipi"), "L'Amazone"),
Question("Qui a découvert l'Amérique ?", ("Christophe Colomb", "Vasco de Gama", "Marco Polo"), "Christophe Colomb"),
Question("Qui a écrit 'Les Misérables' ?", ("Victor Hugo", "Gustave Flaubert", "Alexandre Dumas"), "Victor Hugo"),
Question("Quel est l'élément le plus abondant dans l'Atmosphère terrestre ?", ("Oxygène", "Azote", "Dioxyde de carbone"), "Azote"),
Question("Qui a peint 'La Nuit étoilée' ?", ("Claude Monet", "Vincent van Gogh", "Salvador Dali"), "Vincent van Gogh"),
Question("Quelle est la plus haute montagne du monde ?", ("Le Mont Everest", "Le K2", "Le Kilimandjaro"), "Le Mont Everest"),
Question("Quel est le plus grand désert du monde ?", ("Le Sahara", "Le désert de Gobi", "Le désert d'Atacama"), "Le Sahara"),
Question("Qui a écrit 'l'Odyssée' ?", ("Homène", "Virgile", "Eschyle"), "Homène"),
Question("Quel est le plus grand mammifère terrestre ?", ("L'éléphant d'Afrique", "L'Ours polaire", "La girafe"), "L'éléphant d'Afrique"),
Question("Qui a inventé la théorie de la relativité ?", ("Isaac Newton", "Albert Einstein", "Stephen Hawking"), "Albert Einstein"),
Question("Quel est le plus grand pays du monde en termes de superficie ?", ("La Russie", "Le Canada", "Les Etats Unis"), "La Russie"),
Question("Qui a peint 'Les Tournesols' ?", ("Claude Monet", "Pablo Picasso", "Vincent van Gogh"), "Vincent van Gogh"),
Question("Quelle est le plus gande chaine de montagne du monde ?", ("Les Aples", "Les Andes", "L'Himalaya"), "L'Himalaya"),
Question("Qui a écrit 'Le petit Prince' ?", ("Antoine de Saint-Exupéry", "Marcel Proust", "Albert Camus"), "Antoine de Saint-Exupéry"),
Question("Quel est le plus grand organe du corps humain ?", ("Le foie", "La peau", "Le cerveau"), "La peau"),
Question("Quelle est la monnaie officielle du Japon ?", ("Le yuan", "Le won", "Le yen"), "Le yen"),
            )

# Programme Principal
print()
print("                         ----------Bienvenue dans ce QCM de 20 questions de cultures générales----------       \n")

# for j in range(0, len(questions)):
 #   print(f"Question n° {j + 1} sur {len(questions)}")

questionnaire = Questionnaire(questions)
questionnaire.lancer()