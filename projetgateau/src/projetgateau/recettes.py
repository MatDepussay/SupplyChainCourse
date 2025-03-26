
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

    def __eq__(self, autre):
        if self.sousProduitFinal == autre.sousProduitFinal and self.sousProduitNecessaires == autre.sousProduitNecessaires:
            return True
        return False


class recette(object):
    def __init__(self, listeEtapes):
        self.listeEtapes:List[etape] = listeEtapes

        self.listeSousProduits:List[sousProduit] = []
        for step in self.listeEtapes:
            if step.sousProduitFinal not in self.listeSousProduits:
                self.listeSousProduits.append(step.sousProduitFinal)

    def verifierValidite(self) -> bool:
        """
        Vérifie si les sous-produits necessaires pour la recette peuvent être obtenu via une étape de la recette.

        Paramètres :
        - Aucun

        Renvoie :
        - booléen : Vrai si la recette est auto-suffisante, faux sinon.
        """
        for step in self.listeEtapes:
            for prerequis in step.sousProduitNecessaires:
                if prerequis not in self.listeSousProduits:
                    return False
        return True

class etapeTemporelle(etape):

    def __init__(self, Etape, tps_debut):
        self.etape = Etape
        self.tps_debut = tps_debut
        self.tps_fin = self.tps_debut + self.etape.duree


class planning(object):

    def __init__(self, listeRecette):
        self.listeRecette:List[recette] = listeRecette

        self.listeSousProduits = []
        for recipe in self.listeRecette:
            self.listeSousProduits += [ prod for prod in recipe.listeSousProduits if prod not in self.listeSousProduits]

        self.listeEtapes = []
        for recipe in self.listeRecette:
            self.listeEtapes += [ step for step in recipe.listeEtapes if step not in self.listeEtapes]

        self.planning : List[List[etapeTemporelle]] = []

    def genererPlanning(self, nb_commis=1):

        graph = dict()
        for sousProduit in self.listeSousProduits:
            L = []
            for step in self.listeEtapes:
                if(step.sousProduitFinal == sousProduit):
                    L += [ produits for produits in step.sousProduitNecessaires if produits not in L]
            graph[sousProduit] = list(L) #<---
        ts = TopologicalSorter(graph)
        triTopo = list(ts.static_order())
        self.planning = []
        
        for prod in triTopo:
            for step in self.listeEtapes:
                if step.sousProduitFinal == prod:
                    self.planning.append(step)

    def __str__(self):
        S = "Ordre possible : \n"
        temps = 0
        for i, step in enumerate(self.planning):
            S+= str(i+1) + ") "+ step.nom + ", duree : "+ str(step.duree) + " min\n"
            temps += step.duree
        S+= "Temps total : "+str(temps)+" min."
        return S
