from projetmine import reseau, data
def run():
    data.load

    for gare in ListeGares:
        gare.loadLignes()
        gare.loadVoisins()

    Menu = 0
    while(True):
        if(Menu == 0):
            print("Que voulez-vous faire ?")
            print("1 - Afficher la carte")
            print("2 - Trouver un trajet")
            print("3 - Quitter")

            result = int(input())

            if(1<= result <= 3):
                Menu = result
            else:
                print("Input invalide")
        elif(Menu == 3):
            break
        elif(Menu == 1):
            affich.afficherCarte()
            Menu=0
        elif(Menu == 2):
            print("Rentrez le nom de la gare de départ :")

            gareDepart = None
            while( not gareDepart):
                result = str(input())
                for gare in ListeGares:
                    if(gare.nom == result):
                        gareDepart = gare
                if( not gareDepart):
                    print("La gare ", result, " n'existe pas ! Réessayez : ")

            print("Rentrez le nom de la gare d'arrivée :")
            gareArrivee = None
            while( not gareArrivee):
                result = str(input())
                for gare in ListeGares:
                    if(gare.nom == result):
                        gareArrivee = gare
                if( not gareArrivee):
                    print("La gare ", result, " n'existe pas ! Réessayez : ")

            Trajet = gareDepart.cheminOptimalVers(gareArrivee)
            print("Le trajet passera par les gares suivantes : ")
            for gare in Trajet[0]:
                print(gare.nom)
            print("Le trajet prendra ", Trajet[1], " minutes.")
            Menu = 0
