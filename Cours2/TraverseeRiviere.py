from rich import print
from enum import Enum
from dataclasses import dataclass

#On importe les deux bibliothèques
import networkx as nx
import matplotlib.pyplot as plt

def main():
    print("Hello from cours2!")

if __name__ == "__main__":
    main()

class Rive(Enum):
    GAUCHE = "gauche"
    DROITE = "droite"

@dataclass(frozen=True, unsafe_hash=True)
class Etat:
    berger: Rive
    loup: Rive
    mouton: Rive
    chou: Rive

etatDepart = Etat(
    berger=Rive.GAUCHE,
    loup=Rive.GAUCHE,
    mouton=Rive.GAUCHE,
    chou=Rive.GAUCHE
)

#print(etatDepart.berger)

etats = []

def listerEtats() -> None:
    eP = [Rive.GAUCHE,Rive.DROITE]
    for i in range(16):
        etat = Etat(
            berger=eP[(i//8)%2],
            loup=eP[(i//4)%2],
            mouton=eP[(i//2)%2],
            chou=eP[i%2]
        )
        if(etat not in etats):
            etats.append(etat)
#print(etats)

def sontVoisins(etat1 : Etat, etat2 : Etat) -> bool:
    if etat1.berger == etat2.berger:
        return False

    nombre_difference = 0
    if etat1.mouton != etat2.mouton:
        nombre_difference += 1
    if etat1.chou != etat2.chou:
        nombre_difference += 1
    if etat1.loup != etat2.loup:
        nombre_difference += 1

    if nombre_difference > 1:
        return False
    return True

def estValide(etat : Etat) -> bool:
    """
    La foncion estValide prend un Etat en paramètre et renvoie True si l'état est valide et False sinon.
    Un état est valide si ni le mouton ni le chou ne sont mangés.

    Example :
    >>>etatV = Etat(
        berger="droite",
        mouton="droite",
        chou="gauche",
        loup="droite"
    )
    >>>estValide(etatV)
    True
    """
    if etat.mouton == etat.loup and etat.mouton != etat.berger:
        return False
    if etat.mouton == etat.chou and etat.mouton != etat.berger:
        return False
    return True

#Créer la liste de tous les états valides !
etatsValides = []
def listerEtatValides() -> None:
    for etat in etats:
        if estValide(etat):
            etatsValides.append(etat)

    print("On a ", len(etatsValides), " états valides.")

#Créer la liste des arrêtes de mon graphe.
arretes = []

def creerListeArretes():
    for etat1 in etatsValides:
        for etat2 in etatsValides:
            if sontVoisins(etat1, etat2):
                if( (etat1,etat2) not in arretes  and (etat2,etat1) not in arretes):
                    arretes.append( (etat1,etat2) )

    print("On a ", len(arretes), " arretes.")


def afficherGraphe():
    #On créé le graphe
    G = nx.Graph() #Non-orienté
    #G = nx.DiGraph() #Orienté

    #On créé les noeuds
    G.add_nodes_from (etatsValides)

    #On ajoute les arrêtes entre les noeuds
    G.add_edges_from(arretes)

    #On dessine le graphe
    nx.draw(G)

    #On peut sauvegarder la figure
    #plt.savefig("basicgraph2.png")

    #Ou juste l'afficher
    plt.show()
