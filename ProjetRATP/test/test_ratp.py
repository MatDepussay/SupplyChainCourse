import pytest

from projetratp.sqlimport import *


loadListeLignes()

loadListeGare()

garePorteDoree = None
gareMaryse = None
gareMontempoivre = None
Bercy = None
Nation = None

for gare in ListeGares:
    gare.loadLignes()
    if(gare.id == 66):
        garePorteDoree = gare
    if(gare.id == 86):
        gareMaryse = gare
    if(gare.id == 85):
        gareMontempoivre = gare
    if(gare.nom == "Bercy"):
        Bercy = gare
    if(gare.nom == "Nation"):
        Nation = gare



def test_loadVoisins():
    garePorteDoree.loadVoisins()
    assert len(garePorteDoree.voisins) == 3
    assert gareMontempoivre in garePorteDoree.voisins

def test_isVoisin():
    assert garePorteDoree.isVoisin(gareMontempoivre)
    assert not garePorteDoree.isVoisin(gareMaryse)
    assert not garePorteDoree.isVoisin(garePorteDoree)

for gare in ListeGares:
    gare.loadVoisins()

def test_trajet():
    TrajetBercyNation = Bercy.cheminOptimalVers(Nation)
    assert len(TrajetBercyNation[0]) == 6
    assert TrajetBercyNation[1] == 10
