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
        self.voisins: List[Gare] = []

    def __str__(self):
        return "Nom : "+self.nom + "\n Lon. "+str(self.x)+" Lat. "+str(self.y)+"\n Lignes : "+str(self.lignes)

    def __eq__(self, other):
        return self.id == other.id

    def __neq__(self, other):
        return self.id != other.id

    def __hash__(self):
        return hash(str(id))

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
                        if autreGare not in self.voisins:
                            self.voisins.append(autreGare)

    def isVoisin(self, autreGare) -> bool:
        return autreGare in self.voisins

    def calculerTrajetVoisin(self,autreGare,derniereGare):
        if not self.isVoisin(autreGare) :
            raise ValueError("Les gares doivent être voisines.")
        if(autreGare == derniereGare):
            return 2
        LigneActuelles = []
        LignePrecedentes = []
        for ligne2 in autreGare.lignes:
            for ligne1 in self.lignes:
                if(ligne1 == ligne2):
                    LigneActuelles.append(ligne1)

            for ligne3 in derniereGare.lignes:
                if(ligne3 == ligne2):
                    LignePrecedentes.append(ligne3)

        for ligne in LignePrecedentes:
            if ligne in LigneActuelles:
                return 2
        return 7

    def cheminOptimalVers(self, autreGare):
        DerniereGare = dict()
        DistancesToSelf = dict()
        for gare in data.ListeGares:
            DistancesToSelf[gare] = float("inf")
        DistancesToSelf[self] = 0
        DerniereGare[self] = self
        Valides = [self]
        Candidats = list(self.voisins)

        compteur = 0
        while autreGare not in Valides:
            if len(Candidats) == 0:
                raise ValueError("Trajet impossible")
            compteur += 1
            #On calcules les distances avec les candidats :
            for gare_candidat in Candidats:
                for gare_valide in Valides:
                    if(gare_valide.isVoisin(gare_candidat)):
                        DistancePotentielle = DistancesToSelf[gare_valide] + gare_candidat.calculerTrajetVoisin(gare_valide,DerniereGare[gare_valide])
                        if DistancePotentielle < DistancesToSelf[gare_candidat]:
                            DistancesToSelf[gare_candidat] = DistancePotentielle
                            DerniereGare[gare_candidat] = gare_valide

            #On valide la plus petite distance
            minValeur = float("inf")
            garemin = None
            for gare_candidat in Candidats:
                if minValeur >= DistancesToSelf[gare_candidat]:
                    minValeur = DistancesToSelf[gare_candidat]
                    garemin = gare_candidat
            Valides.append(garemin)
            Candidats.remove(garemin)

            #On ajoute les nouveaux candidats
            for gare in garemin.voisins:
                if gare not in Valides and gare not in Candidats:
                    Candidats.append(gare)


        #On return le chemin
        Chemin = [autreGare]
        while Chemin[-1] != self:
            Chemin.append(DerniereGare[Chemin[-1]])

        Chemin.reverse()
        return (Chemin, DistancesToSelf[Chemin[-1]])




@dataclass(frozen=True, unsafe_hash=True)
class Ligne:
    gares: List[Gare] #liste de gares ordonnée par ordre de numéro d'arret
    id: str
    nom: str
    type: str
