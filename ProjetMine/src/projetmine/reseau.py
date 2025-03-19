from typing import Tuple, List



type Transformation = List[Tuple(str,str), int]

class Entreprise(object):

    def __init__(self,nom,listeTransformations=[]):
        self.nom : str = nom
        self.transformations : List[Transformation] = listeTransformations

    def ajouterTransfo(self, transfo : Transformation):
        if transfo[0] in [tf[0] for tf in self.transformations]:
            for i,tf in enumerate(self.transformations):
                if(transfo[0] == tf[0]):
                    self.transformations[i][1] = transfo[1]
        else:
            self.transformations.append(transfo)

    def __eq__(self, other):
        return self.nom == other.nom

    def __str__(self):
        S = "L'entreprise " + self.nom + " produit :\n"
        for transfo in self.transformations:
            S+= transfo[0][0] + " --> " + transfo[0][1] + "( max : "+ str(transfo[1])+")\n"
        return S

ListeMatieres : List[str] = ["Minerai de fer", "Acier brut",
                "Acier raffiné", "Quincaillerie",
                "Plaques d'acier", "Pièces automobiles"]

ListeEntreprises : List[Entreprise] = [Entreprise("A",[[("Minerai de fer", "Acier brut"),530]]),
                                        Entreprise("B",[[("Minerai de fer", "Acier raffiné"), 4000]])]



CapaciteDeTransformation = [[("Minerai de fer","Acier brut"),530]]
