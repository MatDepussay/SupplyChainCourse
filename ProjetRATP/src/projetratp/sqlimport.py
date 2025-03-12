
import projetratp.ratp as ratp
from typing import List
import sqlite3

ListeGares : List[ratp.Gare] = []

ListeLignes : List[ratp.Ligne] = []

def loadListeGare()-> None:
    """
    Charge la liste des gares à partir de la base de données.
    """
    conn = sqlite3.connect('RATPnetwork.db')

    cur = conn.cursor()
    result = cur.execute("SELECT * FROM gares")

    for row in result:
        nouvelleGare = ratp.Gare(nom = row[1], id = row[0], coord=(row[2],row[3]))
        ListeGares.append(nouvelleGare)

    conn.close()

def loadListeLignes() -> None:
    """
    Charge la liste des lignes de transport à partir de la base de données.
    """
    conn = sqlite3.connect('RATPnetwork.db')

    cur = conn.cursor()
    result = cur.execute("SELECT * FROM lignes")

    for row in result:
        nouvelleLigne = ratp.Ligne(gares=[],id=row[0],nom=row[1],type=row[2])
        ListeLignes.append(nouvelleLigne)

    cur2 = conn.cursor()
    result2 = cur2.execute("SELECT * FROM gares_lignes ORDER BY id_ligne DESC, numArret")

    for row in result2:
        for ligne in ListeLignes:
            if (row[1] == ligne.id):
                ligne.gares.append(row[0])

    conn.close()
