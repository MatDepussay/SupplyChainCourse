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
    if(gare.id == 66):
        gareDepart = gare
    if(gare.id == 86):
        gareArrivee = gare

print(ListeLignes[0])
print(gareDepart)
print(gareArrivee)
