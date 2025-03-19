from projetratp.sqlimport import *
import networkx as nx
import matplotlib.pyplot as plt


loadListeLignes()
print(ListeLignes)

loadListeGare()

for gare in ListeGares:
    gare.loadLignes()
    gare.loadVoisins()
    print(gare)


#On créé le graphe
G = nx.Graph() #Non-orienté
#G = nx.DiGraph() #Orienté

#On créé les noeuds
G.add_nodes_from (ListeGares)

#On ajoute les arrêtes entre les noeuds
ListeArretes = []
for index, gare1 in enumerate(ListeGares):
    for gare2 in ListeGares[(index + 1):]:
        if gare1.isVoisin(gare2):
            ListeArretes.append((gare1,gare2))
print(ListeArretes)
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
