from typing import Tuple
from typing import List
import projetratp.sqlimport as data
from dataclasses import dataclass

class Gare(object):

    def __init__(self, nom:str, id:int, coord:Tuple[float,float]):
        self.nom:str = nom
        self.id:int = id
        self.lignes: list = []
        self.voisins: list = []
        self.x:float = coord[0]
        self.y:float = coord[1]

    def __str__(self):
        return "Nom : "+self.nom + "\n Lon. "+str(self.x)+" Lat. "+str(self.y)
    
    def loadLignes(self):
        if (len(data.ListeLignes) == 0):
            raise ValueError("Liste des lignes non chargée")
        else:
            for ligne in data.ListeLignes:
                if self.id in ligne.gares:
                    self.lignes.append(ligne.id)
    def loadVoisins(self):
        for autreGare in data.ListeGare:
            for ligne in data.ListeLignes:
                if autreGare.id in ligne.gares and self.id in ligne.gares :
                    if abs(ligne.gares.index(self.id) -ligne.gares.index(autreGare.id)) == 1:
                        self.voisins.append(autreGare.id)

    def isVoisin(self, autreGare):
       return autreGare.id in self.voisins

@dataclass(frozen=True,unsafe_hash=True)
class Ligne:
    gares : List[Gare]
    id: str
    nom : str
    type : str
