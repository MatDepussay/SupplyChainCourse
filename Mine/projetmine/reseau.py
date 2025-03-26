from typing import Tuple, List
import scipy as sp


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
        else:
            self.transformation.append(transfo)

    def __eq__(self, other):
        return self.nom==other.nom
    
    def __str__(self):
        S = "L'entreprise "+self.nom+" produit\n"
        for transfo in self.transformation:
            S+=transfo[0][0]+" -> "+transfo[0][1]+"( max: "+str(transfo[1])+")\n"

        return S
    
ListeMatieres : List[str]
ListeEntreprise : List[Entreprise]
ListeTransformation : List[Transformation]



def calculerFlotMaximal():
        matriceAdjacence = [[0 for _ in ListeMatieres]for _ in ListeMatieres]
        for transfo in ListeTransformation:
            for i in range(len(ListeMatieres)):
                if (ListeMatieres[i]==transfo[0][0]):
                    for j in range(len(ListeMatieres)):
                        if(ListeMatieres[j]==transfo[0][1]):
                            matriceAdjacence[i][j]=transfo[1]
                            break
                    break

        MatriceCsArray = sp.sparse.csr_matrix(matriceAdjacence)
        index_source=0
        for i in range(len(ListeMatieres)):
            if (ListeMatieres[i]==matiere_puits):
                index_source = i
                break


        result= sp.sparse.csgraph.maximum_flow(MatriceCsArray, 0, 5)


ListeEntreprise : List[Entreprise] = [Entreprise("A", [[("Minerai de fer", "Acier Brut"), 530]]),
                                      Entreprise("B", [[("Minerai de fer", "Acier raffiné"), 4000]])]
CapaciteDeTransformation=[[("Minerai de fer", "Acier Brut"),530]]

