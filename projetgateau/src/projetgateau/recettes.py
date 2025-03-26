
from typing import List

class sousProduit(object):

    def __init__(self, nom:str):
        self.nom :str = nom



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
