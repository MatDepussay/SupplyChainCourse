from typing import Tuple, List
from dataclasses import dataclass
import projetratp.sqlimport as data

class Gare(object):

    def __init__(self, nom:str, id:int, coord:Tuple[float,float]):
        self.nom:str = nom
        self.id:int = id
        self.x:float = coord[0]
        self.y:float = coord[1]
        self.lignes: List[str] = []
        self.voisins: List[int] = []

    def __str__(self):
        return "Nom : "+self.nom + "\n Lon. "+str(self.x)+" Lat. "+str(self.y)+"\n Lignes : "+str(self.lignes)

    def loadLignes(self) -> None:
        if( len(data.ListeLignes) == 0):
            raise ValueError("Charger la liste des lignes avant d'executer isVoisin.")
        for ligne in data.ListeLignes:
            if self.id in ligne.gares:
                self.lignes.append(ligne.id)

    def loadVoisins(self) -> None:
        if( len(data.ListeLignes) == 0 or len(data.ListeGares) == 0):
            raise ValueError("Charger les listes des lignes et des gares avant d'executer isVoisin.")
        for autreGare in data.ListeGares:
            for ligne in data.ListeLignes:
                if (autreGare.id in ligne.gares and self.id in ligne.gares):
                    if abs(ligne.gares.index(self.id) - ligne.gares.index(autreGare.id)) == 1:
                        self.voisins.append(autreGare.id)

    def isVoisin(self, autreGare) -> bool:
        return autreGare.id in self.voisins



@dataclass(frozen=True, unsafe_hash=True)
class Ligne:
    gares: List[Gare] #liste de gares ordonnée par ordre de numéro d'arret
    id: str
    nom: str
    type: str
