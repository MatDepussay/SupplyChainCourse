from typing import Tuple, List



ListeMatieres = ["Minerai de fer", "Acier Brut", "Acier raffiné", "quincaillerie","Plaque d'acier", "pieces automobiles"]

type Transformation = List[Tuple[str, str], int]

class Entreprise:
    def __init__(self,nom,listeTransformation):
        self.nom :str =nom
        self.transformation : List[Transformation] =listeTransformation

    def ajouterTransfo(self,transfo:Transformation):
        if transfo[0] in [tf[0] for tf in self.transformation]:
            for i,tf in enumerate(self.transformation):
                if transfo[0]==tf[0]:
                    self.transformation[i]=transfo[1]
                    tf[1]= transfo[1]


    def __str__(self):
        S = "L'entreprise "+self.nom+" produit\n"
        for transfo in self.transformation:
            S+=transfo[0][0]+" -> "+transfo[0][1]+"( max: "+str(transfo[1])+")\n"

ListeEntreprise : List[Entreprise] = [Entreprise("A", [[("Minerai de fer", "Acier Brut"), 530]]),
                                      Entreprise("B", [[("Minerai de fer", "Acier raffiné"), 4000]])]
CapaciteDeTransformation=[[("Minerai de fer", "Acier Brut"),530]]