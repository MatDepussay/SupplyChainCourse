from projetratp.sqlimport import *
import networkx as nx
import matplotlib.pyplot as plt


loadListeGare()

for gare in ListeGare:
    print(gare)


#On créé le graphe
G = nx.Graph() #Non-orienté
#G = nx.DiGraph() #Orienté

#On créé les noeuds
G.add_nodes_from (ListeGare)

#On ajoute les arrêtes entre les noeuds
ListeArretes = []
G.add_edges_from(ListeArretes)

pos = dict()
for gare in ListeGare:
    pos[gare] = [gare.x,gare.y]
#On dessine le graphe
nx.draw(G, pos)

#Ou juste l'afficher
plt.show()
