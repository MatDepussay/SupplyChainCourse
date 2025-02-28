from TraverseeRiviere import *

listerEtats()

def test_listerEtats():
    assert len(etats) == 16

listerEtatValides()

def test_listerEtatsValides():
    assert len(etatsValides) == 10

def test_estValide():
    etatV = Etat(
        berger="droite",
        mouton="droite",
        chou="gauche",
        loup="droite"
    )
    etatPV = Etat(
        berger="gauche",
        mouton="droite",
        chou="gauche",
        loup="droite"
    )
    assert estValide(etatV)
    assert not estValide(etatPV)
