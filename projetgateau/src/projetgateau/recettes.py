
from typing import List

class sousProduit(object):

    def __init__(self, nom:str):
        self.nom :str = nom

    def __eq__(self, autre):
        return self.nom == autre.nom
    
    def __hash__(self):
        return hash(self.nom)

class etape(object):

    def __init__(self, nomEtape:str, produitFinal:sousProduit, duree:int,
                    sousProduitNecessaires: List[sousProduit] = [],
                    besoinFour:bool = False, etapeActive:bool = True ):
        self.nom :str = nomEtape
        self.besoinFour :bool = besoinFour
        self.duree:int = duree
        self.active: bool = etapeActive
        self.sousProduitFinal: sousProduit = produitFinal
        self.sousProduitNecessaires : List[sousProduit] = sousProduitNecessaires

class recette(object):
    pass

class planing(object):
    pass