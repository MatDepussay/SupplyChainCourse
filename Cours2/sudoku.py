from typing import List, Tuple

type grille = List[List[int]]

Magrille : grille = [[1,2,3],[0,-5]]

def checkIntegrity(grid : grille) -> None:
    assert len(grid) == 9
    for ligne in grid:
        assert len(ligne) == 9
        for num in ligne:
            assert 0 <= num <= 9
            