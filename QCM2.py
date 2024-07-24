class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse
        
        
    def demander_nombre_numerique_utilisateur(self, min, max):
        choix_str = input(f"Quel est votre réponse entre ({min} et {max}) : ")
        try:
            choix_int = int(choix_str)
            if min <= choix_int <= max:
                return choix_int
            print(f"SVP: Entrer un nombre entre ({min} et {max})\n")
            return self.demander_nombre_numerique_utilisateur(min, max)
        except:
            print("Veuillez entrer un nombre numérique\n")
            return self.demander_nombre_numerique_utilisateur(min, max) 



    def poser_question(self):
        reponse = self.choix
        bonne_reponse = self.bonne_reponse
        print("Question:")
        print("       ", self.titre)
        for i in range(len(reponse)):
            nb = i + 1
            print("   ", nb, "-", reponse[i])
        
        reponse_question = False
        choix_int = self.demander_nombre_numerique_utilisateur(1, len(reponse))
        if reponse[choix_int - 1] == bonne_reponse:
            print("Bonne reponse")
            reponse_question = True
        else:
            print("Mauvaise réponse")
            print()
            return reponse_question
            


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions
        
        
    def lancer_programme(self):
        score = 0
        for question in questions:
            if question.poser_question():
                score += 1
        print(f"Votre score finale est {score} / {len(self.questions)}")




questions = [
    Question("Qui est l'homme le plus riche du monde en 2024 ?", ("Elon Musk", "Warren Buffet", "Mark Zuckerberg"), "Elon Musk"),
    ]



questionnaire = Questionnaire(questions)
questionnaire.lancer_programme()

