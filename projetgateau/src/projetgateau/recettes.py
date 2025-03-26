
from typing import List
from graphlib import *
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
    def __init__(self, listeEtapes): 
        self.listeEtapes:List[etape] = listeEtapes
        self.listeSousProduits:List[sousProduit] = []
        for step in self.listeEtapes:
            if step.sousProduitFinal not in self.listeSousProduits:
                self.listeSousProduits.append(step.sousProduitFinal)
    def verifierValide(self):
        listePrerequis = []
        for step in self.listeEtapes:
            for prerequis in step.sousProduitNecessaires:
                if prerequis not in self.listeSousProduits:
                    return False
        return True

        


class planing(object):
    def __init__(self, listeRecette):
        self.listeRecettes = listeRecette
        self.listeSousProduits = []
        for recipe in self.listeRecettes:
            self.listeSousProduits += [prod for prod in recipe.listeSousProduits if prod not in self.listeSousProduits]
            self.listeSousProduits = []
        self.listeEtapes = []
        for recipe in self.listeRecettes:
            self.listeEtapes += [step for step in recipe.listeEtapes if step not in self.listeEtapes]
        self.planing :List[etape]= []
    
    def genererplaning(self):
        graph =dict()
        for sousProduits in self.listeSousProduits:
            L=[]
            for step in self.listeEtapes:
                if(step.sousProduitFinal == sousProduits):
                        L += [produits for produits in step.sousProduitNecessaires if produits not in L]
        graph[sousProduits] = list(L)
        ts=TopologicalSorter(graph)
        self.planing = list(ts.static_order())
    def __str__(self):
        S="Ordre possible : "
        for i, prod in enumerate(self.planing):
            S+=str(i=1)+ ") "+prod.nom+ "\n"
        return S

