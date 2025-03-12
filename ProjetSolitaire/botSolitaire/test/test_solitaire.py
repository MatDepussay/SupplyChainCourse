import botsolitaire.solitaire as bot
import pytest

PlateauTest1 = bot.Plateau(
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
)

PlateauTest2 = bot.Plateau(
    [
        [1, 13, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, "Bonjour", 1],
    ]
)


def test_estValide():
    with pytest.raises(ValueError):
        bot.Plateau(
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 2, 1, 1, 1, 1],
            ]
        )


PlateauTest4 = bot.Plateau(
    [
        [1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
)

PlateauTest5 = bot.Plateau(
    [
        [1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
    ]
)

def test_str():
    print(PlateauTest1)

def test_eq():
    assert PlateauTest1 == PlateauTest2
    assert not PlateauTest1 == PlateauTest4


def test_hash():
    assert hash(PlateauTest1) == hash(PlateauTest2)
    assert not hash(PlateauTest1) == hash(PlateauTest4)


coupValide = [(3, 1), (3, 3)]


def test_mouvementValide():
    assert PlateauTest4.mouvementValide(coupValide)
    assert not PlateauTest4.mouvementValide([(4, 2), (4, 0)])  # case arrivee
    assert not PlateauTest4.mouvementValide([(4, 2), (3, 3)])  # diagonale
    assert not PlateauTest4.mouvementValide([(3, 5), (3, 3)])  # case depart
    assert not PlateauTest4.mouvementValide([(1, 3), (3, 3)])  # case du milieu
    assert not PlateauTest4.mouvementValide([(0, 3), (3, 3)])  # saut de 2
    assert not PlateauTest4.mouvementValide([(0, 0), (0, 2)])
    assert not PlateauTest4.mouvementValide([(0, 2), (0, 0)])


def test_coupsPossibles():
    assert len(PlateauTest1.coupsPossibles()) == 4

def test_genererVoisins():
    assert len(PlateauTest4.genererVoisins()) == 7
    assert len(PlateauTest5.genererVoisins()) == 7
    assert len(PlateauTest1.genererVoisins()) == 4

PlateauTest6 = bot.Plateau(
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
)

def test_jouerCoup():
    assert PlateauTest6 == PlateauTest1.jouerCoup([(3,5),(3,3)])


Depart2 = bot.Plateau(
    [
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
)

Final = bot.Plateau(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
)

Impossible = bot.Plateau(
    [
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
    ]
)

def test_resoudre():
    assert len(bot.resoudreSolitaire(Depart2,Final)) == 3
    with pytest.raises(ValueError):
        bot.resoudreSolitaire(Impossible, Final)
