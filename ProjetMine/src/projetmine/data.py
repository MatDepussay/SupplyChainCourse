import csv
import projetmine.reseau as reseau

def load_matieres():
    reseau.ListeMatieres = []
    for entreprise in reseau.ListeEntreprises:
        for transfo in entreprise.transformations:
            if transfo[0][0] not in reseau.ListeMatieres:
                reseau.ListeMatieres.append(transfo[0][0])
            if transfo[0][1] not in reseau.ListeMatieres:
                reseau.ListeMatieres.append(transfo[0][1])

def load_transformations():
    reseau.listeTransformations = []
    for entreprise in reseau.ListeEntreprises:
        for transfo in entreprise.transformations:
            if transfo[0] not in reseau.listeTransformations:
                reseau.listeTransformations.append(transfo)
            else:
                for i in range(len(reseau.listeTransformations)):
                    if reseau.listeTransformations[i][0] == transfo[0]:
                        reseau.listeTransformations[i][1] += transfo[1]

def load_entreprises():
    with open('data_entreprises.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        reseau.ListeEntreprises = []
        for row in spamreader:
            if(reseau.Entreprise(row[0]) in reseau.ListeEntreprises):
                for i,entrep in enumerate(reseau.ListeEntreprises):
                    if(entrep == reseau.Entreprise(row[0])):
                        reseau.ListeEntreprises[i].ajouterTransfo([(row[1],row[2]), int(row[3])])
            else:
                reseau.ListeEntreprises.append(reseau.Entreprise(row[0],[[(row[1],row[2]), int(row[3])]]))
    load_matieres()
    load_transformations()
    
def save():
    with open('data_entreprises.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for entreprise in reseau.ListeEntreprises:
            for transfo in entreprise.transformations:
                spamwriter.writerow([entreprise.nom,transfo[0][0],transfo[0][1],transfo[1]])
    print("Sauvegardé avec succès !")
