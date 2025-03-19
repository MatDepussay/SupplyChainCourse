from typing import Tuple
from typing import List
import projetratp.sqlimport as data
from dataclasses import dataclass

class Gare(object):

    def __init__(self, nom:str, id:int, coord:Tuple[float,float]):
        self.nom:str = nom
        self.id:int = id
        self.lignes: list = []
        self.voisins: list[Gare] = []
        self.x:float = coord[0]
        self.y:float = coord[1]
    def __eq__(self, other):
        return self.id == other.id
    def __neq__(self, other):
        return self.id != other.id
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

    def calculerTrajetVOisin(self, autreGare):
        if self.isVoisin(autreGare):
            return 2
        raise ValueError("Les doivent etre voisines")

    def cheminoptimalVers(self, autreGare):
        DerniereGare = dict()
        ListeGareId= [gare.id for gare in data.ListeGare]
        DistanceToSelf= float("int")
        DistanceToSelf[self]=0
        Valides=[self]
        Candidats=self.voisins
        while autreGare not in Valides:
            for gare_candidats in Candidats:
                for gare_valide in Valides:
                   if (gare_valide.isVoisin(gare_candidats)):
                       DistancePotentielle = DistanceToSelf[gare_valide]+gare_valide.calculerTrajetVOisin(gare_valide,gare_candidats)
                       if DistancePotentielle < DistanceToSelf[gare_candidats]:
                           DistanceToSelf[gare_candidats]=DistancePotentielle
            minValeurs= float("int")
            garemin= None
            for gare_id in Candidats:
                if minValeurs>= DistanceToSelf[self.id]:
                    minValeurs=DistanceToSelf[self.id]
                    garemin=gare_candidats
            Valides.append(garemin)
            Candidats.remove(garemin)

            for gare in garemin.voisins:
                if garemin not in Valides and gare not in Candidats:
                    Candidats.append(garemin)

            Chemin = [autreGare]
            while Chemin[-1] != self:
                Chemin.append(DerniereGare[Chemin[-1]])

@dataclass(frozen=True,unsafe_hash=True)
class Ligne:
    gares : List[Gare]
    id: str
    nom : str
    type : str

