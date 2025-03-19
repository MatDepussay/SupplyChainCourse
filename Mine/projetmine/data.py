import csv
import projetmine.reseau as reseau

def load():
    with open('data_entreprises.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        reseau.ListeEntreprise = []
        for row in spamreader:
            if(reseau.Entreprise(row[0]) in reseau.ListeEntreprise):
                for i, entrep in enumerate(reseau.ListeEntreprise):
                    if entrep == Entreprise(row[0]):
                        reseau.ListeEntreprise[i].ajouterTransfo([(row[1], row[2]), int(row[3])])
            else:
                reseau.ListeEntreprise.append(Entreprise(row[0], [[(row[1], row[2]), int(row[3])]]))

def save():
    with open('data_entreprises.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for entreprise in reseau.ListeEntreprise:
            for transfo in entreprise.transformations:
                spamwriter.writerow(entreprise.nom,transfo[0][0],transfo[0][1],transfo[1])
    print("Sauvegardé avec succés !")