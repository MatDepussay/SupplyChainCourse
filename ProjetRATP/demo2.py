from projetratp.sqlimport import *
import networkx as nx
import matplotlib.pyplot as plt


loadListeLignes()

loadListeGare()



gareDepart = None
gareArrivee = None

for gare in ListeGares:
    gare.loadLignes()
    gare.loadVoisins()
    if(gare.nom == "Bercy"):
        gareDepart = gare
    if(gare.nom == "Nation"):
        gareArrivee = gare


print(gareDepart)
print(gareArrivee)

print("Chemin : ")

gareDepart.cheminOptimalVers(gareArrivee)
