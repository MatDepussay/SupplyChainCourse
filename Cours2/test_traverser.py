from traverserriviere import *

listerEtats()

def test_listerEtats():
    assert len(etats) == 16


def test_listerEtatsValides():
    assert len(etatsValides) == 10

def test_estValide():
    etatV = Etat(berger="droite",
                 loup="droite",
                mouton="droite",
                chou="gauche")
    etatPV = Etat(berger="gauche",
                  mouton="droite",
                  loup="droite",
                  chou="gauche")
    assert estValide(etatV)
    assert not estValide(etatPV)