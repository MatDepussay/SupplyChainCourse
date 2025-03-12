from projetratp.sqlimport import *
import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore


loadListeGare()

LoadListeLignes()


print(ListeLignes)

for gare in ListeGare:
    gare.loadLignes()
    gare.loadVoisins()
    print(gare)


#On créé le graphe
G = nx.Graph() #Non-orienté
#G = nx.DiGraph() #Orienté

#On créé les noeuds
G.add_nodes_from (ListeGare)

#On ajoute les arrêtes entre les noeuds
ListeArretes = []
for index, gare1 in enumerate(ListeGare):
    for gare2 in ListeGare[index+1:]:
        if gare1.isVoisin(gare2):
            ListeArretes.append((gare1,gare2))
G.add_edges_from(ListeArretes)

pos = dict()
labels = dict()
for gare in ListeGare:
    pos[gare] = [gare.x,gare.y]
    labels[gare] = gare.nom
#On dessine le graphe
nx.draw(G, pos, with_labels=True, labels=labels)

#Ou juste l'afficher
plt.show()
