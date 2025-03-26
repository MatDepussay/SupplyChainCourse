
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

class etapeTemporelle(object):

    def __init__(self, Etape : etape, tps_debut : int):
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

    def genererPlanning(self, nb_commis = 1):

        graph = dict()
        for sousProduit in self.listeSousProduits:
            L = []
            for step in self.listeEtapes:
                if(step.sousProduitFinal == sousProduit):
                    L += [ produits for produits in step.sousProduitNecessaires if produits not in L]
            graph[sousProduit] = list(L) #<---
        ts = TopologicalSorter(graph)
        triTopo = list(ts.static_order())


        self.planning = [[],[]] + [[] for _ in range(nb_commis)]
        """
        [0] -> Ligne du four
        [1] -> Attente
        [2] -> Commis numéro 1
        [3] -> Commis numéro 2
        ...
        """
        tempsActuel = 0
        for prod in triTopo:
            for step in self.listeEtapes:
                if step.sousProduitFinal == prod:
                    #Test prerequis satisfaits

                    for prerequis in step.sousProduitNecessaires:
                        PrerequisTrouve = False
                        for ligne2 in self.planning:
                            for etapeEnCours in ligne2:
                                if prerequis == etapeEnCours.etape.sousProduitFinal:
                                    PrerequisTrouve = True
                                    if(etapeEnCours.tps_fin > tempsActuel):
                                        tempsActuel = etapeEnCours.tps_fin
                        if(not PrerequisTrouve):
                            print("Probleme")

                    if step.besoinFour:
                        #Test si four disponible
                        if len(self.planning[0]) != 0:
                            if(self.planning[0][-1].tps_fin > tempsActuel):
                                tempsActuel = self.planning[0][-1].tps_fin

                        etapeTempo = etapeTemporelle(step,tps_debut =tempsActuel)
                        self.planning[0].append(etapeTempo)
                    elif not step.active:
                        etapeTempo = etapeTemporelle(step,tps_debut =tempsActuel)
                        self.planning[1].append(etapeTempo)
                    else:
                        if len(self.planning[2]) != 0:
                            if(self.planning[2][-1].tps_fin > tempsActuel):
                                tempsActuel = self.planning[2][-1].tps_fin
                        etapeTempo = etapeTemporelle(step,tps_debut =tempsActuel)
                        self.planning[2].append(etapeTempo)


    def __str__(self):
        S = "Ordre possible : \n"
        maxTemps = 0
        for ligne in self.planning:
            for i, step in enumerate(ligne):
                S+= "[ "+ str(step.tps_debut) + " - "+ step.etape.nom + " - "+ str(step.tps_fin) + " ]"
            S += "\n"
            if(ligne[-1].tps_fin > maxTemps):
                maxTemps = ligne[-1].tps_fin
        S+= "Temps total : "+str(maxTemps)+" min."
        return S
