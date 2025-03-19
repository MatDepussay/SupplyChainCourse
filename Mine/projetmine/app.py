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
            print("Renrez le nom de l'entreprise")
            result = ""
            NouvelleEntreprise = reseau.Entreprise(result)
            resultatValide = False
            while(not resultatValide):
                if(result ==""):
                    print("Entrez un nom d'au moins 1 caractere! \n")
                    resultatValide = False
                elif(NouvelleEntreprise in reseau.ListeEntreprise):
                    print("Ce nom d'entreprise existe déjà! \n")
                    resultatValide = False
                else:
                    resultatValide = True
            resultatValide = False
            while(not resultatValide):
                print("Enrtez une transofrmation effectué par l'entreprise : \n")
                print("Matière 1 : ")
                result1 = str(input())
                print("Matière 2 : ")
                result2 = str(input())
                print("Capacité de transformation : ")
                result3 = int(input())
                NouvelleEntreprise.ajouterTransfo([(result1, result2), result3])
                print("Voulez-vous ajouter une autre transformation ? (O/N)")
                result4 =2
                while not(0<=result4<=1):
                    result4= int(input())
                    if(not (0<=result4<=1)):
                        print("Input invalide")
                if(result4 == 0):
                    resultatValide = True
                else:
                    resultatValide = False
    
            reseau.ListeEntreprise.append(NouvelleEntreprise)
            data.save()
            Menu = 0
