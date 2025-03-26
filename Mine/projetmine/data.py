import csv
import projetmine.reseau as reseau


def load_matieres():
    for entreprise in reseau.ListeEntreprise:
        for transfo in entreprise.transformations:
            if transfo[0][0] not in reseau.ListeMatieres:
                reseau.ListeMatieres.append(transfo[0][0])
            if transfo[0][1] not in reseau.ListeMatieres:
                reseau.ListeMatieres.append(transfo[0][1])

def load_transformations():
        reseau.ListeTransformation = []
        for entreprise in reseau.ListeEntreprise:
            for transfo in entreprise.transformations:
             if transfo[0] not in reseau.ListeTransformation:
                reseau.ListeTransformation.append(transfo)
             else:
                 for i in range(len(reseau.ListeTransformation)):
                     if reseau.ListeTransofrmation[i][0] == transfo[0]:
                         reseau.ListeTransformation[i][1] += transfo[1]

def load_entreprise():
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