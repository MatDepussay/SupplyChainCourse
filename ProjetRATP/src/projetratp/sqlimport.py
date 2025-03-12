
import projetratp.ratp as ratp
from typing import List
import sqlite3

ListeGare : List[ratp.Gare] = []

def loadListeGare()-> None:
    """
    Charge la liste des gares à partir de la base de données.
    """
    conn = sqlite3.connect('RATPnetwork.db')

    cur = conn.cursor()
    result = cur.execute("SELECT * FROM gares")

    for row in result:
        nouvelleGare = ratp.Gare(nom = row[1], id = row[0], coord=(row[2],row[3]))
        ListeGare.append(nouvelleGare)

    conn.close()
