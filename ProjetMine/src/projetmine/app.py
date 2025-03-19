from projetmine import reseau, data

def run():
    data.load_entreprises()

    Menu = 0
    while(True):
        if(Menu == 0):
            print("Que voulez-vous faire ?")
            print("1 - Afficher la liste des entreprises")
            print("2 - Ajouter une entreprise")
            print("3 - Modifier une entreprise")
            print("4 - Calculer la demande maximale")
            print("5 - Quitter")

            result = int(input())

            if(1<= result <= 3):
                Menu = result
            else:
                print("Input invalide")
        elif(Menu == 4):
            break
        elif(Menu == 1):
            for entreprise in reseau.ListeEntreprises:
                print(entreprise)
            Menu=0
        elif(Menu == 2):
            print("Rien.")
            Menu = 0
