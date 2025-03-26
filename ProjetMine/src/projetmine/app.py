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
            print("4 - Calculer la demande maximale d'une matière")
            print("5 - Quitter")

            result = int(input())

            if(1<= result <= 5):
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
            result = ""
            resultatValide = False
            while(not resultatValide):
                print("Rentrez le nom de l'entreprise : ")
                result = str(input())
                NouvelleEntreprise = reseau.Entreprise(result)
                if(result == ""):
                    print("Entrez un nom d'au moins 1 caractère !\n")
                    resultatValide = False
                elif(NouvelleEntreprise in reseau.ListeEntreprises):
                    print("L'entreprise existe déjà !\n")
                    resultatValide = False
                else:
                    resultatValide = True

            resultatValide = False
            while(not resultatValide):
                print("Entrez une transformation effectuée par l'entreprise : \n")
                print("Matière 1 : ")
                result1 = str(input())
                print("Matière 2 : ")
                result2 = str(input())
                print("Capacité : ")
                result3 = int(input())
                NouvelleEntreprise.ajouterTransfo([(result1,result2), result3])
                print("Voulez-vous ajouter une autre transformation ? (0=oui/1=non)\n")
                result4 = 2
                while not (0<=result4<=1):
                    result4 = int(input())
                    if(not (0<=result4<=1)):
                        print("Input invalide")
                if(result4 == 0):
                    resultatValide = False
                else:
                    resultatValide = True

            reseau.ListeEntreprises.append(NouvelleEntreprise)
            data.save()
            Menu = 0
