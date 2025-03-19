from typing import Tuple, List
import scipy as sp
import numpy as np


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

ListeMatieres : List[str]

ListeEntreprises : List[Entreprise]

listeTransformations : List[Transformation]

def calculerFlotMaximal(matiere_source, matiere_puits):

    matriceAdjacence = [[0 for _ in ListeMatieres] for _ in ListeMatieres]
    for transfo in listeTransformations:
        for i in range(len(ListeMatieres)):
            if(ListeMatieres[i] == transfo[0][0]):
                for j in range(len(ListeMatieres)):
                    if(ListeMatieres[j] == transfo[0][1]):
                        matriceAdjacence[i][j] = transfo[1]
                        break
                break


    MatriceCsArray = sp.sparse.csr_array(matriceAdjacence)

    index_source = 0
    for i in range(len(ListeMatieres)):
        if(ListeMatieres[i] == matiere_source):
            index_source = i
            break

    index_puits = 0
    for i in range(len(ListeMatieres)):
        if(ListeMatieres[i] == matiere_puits):
            index_puits = i
            break

    result = sp.sparse.csgraph.maximum_flow(MatriceCsArray,index_source,index_puits)

    print(result)
    return(result.flow_value)
