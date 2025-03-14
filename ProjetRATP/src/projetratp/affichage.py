from projetratp.sqlimport import *
import networkx as nx
import matplotlib.pyplot as plt


def afficherCarte():
    G = nx.Graph()

    G.add_nodes_from (ListeGares)

    ListeArretes = []
    for index, gare1 in enumerate(ListeGares):
        for gare2 in ListeGares[(index + 1):]:
            if gare1.isVoisin(gare2):
                ListeArretes.append((gare1,gare2))
    G.add_edges_from(ListeArretes)

    pos = dict()
    labels = dict()
    for gare in ListeGares:
        pos[gare] = [gare.x,gare.y]
        labels[gare] = gare.nom
    #On dessine le graphe
    nx.draw(G, pos, with_labels =True, labels=labels)

    #Ou juste l'afficher
    plt.show()
