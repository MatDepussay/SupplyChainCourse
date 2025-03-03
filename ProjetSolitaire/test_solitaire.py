from solitaire import *
import pytest

def test_estValide():
    PlateauTest1 = Plateau([  [1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1],
                        [1,1,1,0,1,1,1],
                        [1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1]])

    PlateauTest2  = Plateau([  [1,13,1,1,1,1,1],
                    [1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1],
                    [1,1,1,0,1,1,1],
                    [1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1],
                    [1,1,1,1,1,'Bonjour',1]])

    with pytest.raises(ValueError):
        PlateauTest3  = Plateau([  [1,1,1,1,1,1,1],
                            [1,1,2,1,1,1,1],
                            ])


PlateauTest4 = Plateau([    [1,1,0,1,1,1,1],
                            [1,1,1,1,1,1,1],
                            [1,1,1,0,1,1,1],
                            [1,1,1,0,1,0,1],
                            [1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1]])

coupValide = [(3,1),(3,3)]

def test_mouvementValide():
    assert PlateauTest4.mouvementValide(coupValide)
    assert not PlateauTest4.mouvementValide([(4,2),(4,0)]) #case arrivee
    assert not PlateauTest4.mouvementValide([(4,2),(3,3)]) #diagonale
    assert not PlateauTest4.mouvementValide([(3,5),(3,3)]) #case depart
    assert not PlateauTest4.mouvementValide([(1,3),(3,3)]) #case du milieu
    assert not PlateauTest4.mouvementValide([(0,3),(3,3)]) #saut de 2
    assert not PlateauTest4.mouvementValide([(0,0),(0,2)])
    assert not PlateauTest4.mouvementValide([(0,2),(0,0)])
