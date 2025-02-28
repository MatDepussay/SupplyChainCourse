from Sudoku import *
import pytest

Magrille : grille = [[1,2,3],[0,-5]]

def test_validity():
    with pytest.raises(AssertionError):
        checkIntegrity(Magrille)
