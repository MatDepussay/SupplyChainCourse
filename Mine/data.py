import csv
import Mine.reseau as reseau

def load():
    with open('data_entreprises.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        reseau.ListeEntreprise = []
        for row in spamreader:
            reseau.ListeEntreprise.append()

def save():
    with open('data_entreprises.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for entreprise in reaseau.ListeEntreprises:
            for transfo in entreprise.transformations:
                spamwriter.writerow(entreprise.nom,transfo[0][0],transfo[0][1],transfo[1])
    print("Sauvegardé avec succés !")