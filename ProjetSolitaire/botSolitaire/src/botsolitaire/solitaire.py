import copy
import time
from typing import List, Tuple
# import pyinstrument

type mouvement = List[Tuple[int, int]]


class Plateau(object):
    def __init__(self, grille):
        self.billes = grille  # 0 -> Pas de bille, 1 -> une bille
        self.estValide()

    def __eq__(self, autrePlateau) -> bool:  # MonPlateau == AutrePlateau ?
        for i in [0, 1, 5, 6]:
            for j in [2, 3, 4]:
                if self.billes[i][j] != autrePlateau.billes[i][j]:
                    return False

        for i in [2, 3, 4]:
            for j in range(7):
                if self.billes[i][j] != autrePlateau.billes[i][j]:
                    return False
        return True

    def __hash__(self):
        chaineCarac: str = ""
        for i in [0, 1, 5, 6]:
            for j in [2, 3, 4]:
                chaineCarac += str(self.billes[i][j])

        for i in [2, 3, 4]:
            for j in range(7):
                chaineCarac += str(self.billes[i][j])
        return hash(chaineCarac)

    def __str__(self):
        chaineCarac = "\n"
        for i in [0, 1]:
            chaineCarac += "  "
            for j in [2, 3, 4]:
                if self.billes[i][j] != 0:
                    chaineCarac += "O"
                else:
                    chaineCarac += "."
            chaineCarac += "\n"

        for i in [2, 3, 4]:
            for j in range(7):
                if self.billes[i][j] != 0:
                    chaineCarac += "O"
                else:
                    chaineCarac += "."
            chaineCarac += "\n"

        for i in [5, 6]:
            chaineCarac += "  "
            for j in [2, 3, 4]:
                if self.billes[i][j] != 0:
                    chaineCarac += "O"
                else:
                    chaineCarac += "."
            chaineCarac += "\n"

        return chaineCarac

    def nbBilles(self) -> int:
        """
        Compte le nombre de billes présentes sur le plateau.

        Example usage :
        >>> PlateauTest1 = Plateau([    [1,1,1,1,1,1,1],
        ...                             [1,1,1,1,1,1,1],
        ...                             [1,1,1,1,1,1,1],
        ...                             [1,1,1,0,1,1,1],
        ...                             [1,1,1,1,1,1,1],
        ...                             [1,1,1,1,1,1,1],
        ...                             [1,1,1,1,1,1,1]])
        >>> PlateauTest1.nbBilles()
        32

        """
        Somme = 0
        for i in [0, 1, 5, 6]:
            for j in [2, 3, 4]:
                if self.billes[i][j] == 1:
                    Somme += 1

        for i in [2, 3, 4]:
            for j in range(7):
                if self.billes[i][j] == 1:
                    Somme += 1
        return Somme

    def mouvementValide(self, mouv: mouvement):  # mouv = [(x,y), (x,y)]
        # Test self.billes out of range
        for i in [0, 1]:
            for j in [0, 1]:
                if mouv[i][j] >= 7 or mouv[i][j] < 0:
                    return False

        # Verifier case arrivee vide :
        if self.billes[mouv[1][0]][mouv[1][1]] != 0:
            return False

        # Verifier case de depart
        if self.billes[mouv[0][0]][mouv[0][1]] == 0:
            return False

        # Verifier case du milieu
        if (
            self.billes[(mouv[0][0] + mouv[1][0]) // 2][(mouv[0][1] + mouv[1][1]) // 2]
            == 0
        ):
            return False

        # Verifier saut de 2
        if abs(mouv[0][0] - mouv[1][0]) != 2 and abs(mouv[0][1] - mouv[1][1]) != 2:
            return False

        # Verifier horizontal ou vertical
        if mouv[0][0] != mouv[1][0] and mouv[0][1] != mouv[1][1]:
            return False

        # Verifier cases dans le plateau
        if mouv[0][0] in [0, 1, 5, 6]:
            if mouv[0][1] not in [2, 3, 4]:
                return False

        if mouv[1][0] in [0, 1, 5, 6]:
            if mouv[1][1] not in [2, 3, 4]:
                return False

        return True

    def coupsPossibles(self) -> list:
        ListeCoups = []
        for i in [0, 1]:
            for j in [2, 3, 4]:
                if self.billes[i][j]:
                    if self.mouvementValide([(i, j), (i + 2, j)]):
                        ListeCoups.append([(i, j), (i + 2, j)])
                    if j == 2:
                        if self.mouvementValide([(i, j), (i, j + 2)]):
                            ListeCoups.append([(i, j), (i, j + 2)])
                    elif j == 4:
                        if self.mouvementValide([(i, j), (i, j - 2)]):
                            ListeCoups.append([(i, j), (i, j - 2)])

        for i in [5, 6]:
            for j in [2, 3, 4]:
                if self.billes[i][j]:
                    if self.mouvementValide([(i, j), (i - 2, j)]):
                        ListeCoups.append([(i, j), (i - 2, j)])
                    if j == 2:
                        if self.mouvementValide([(i, j), (i, j + 2)]):
                            ListeCoups.append([(i, j), (i, j + 2)])
                    elif j == 4:
                        if self.mouvementValide([(i, j), (i, j - 2)]):
                            ListeCoups.append([(i, j), (i, j - 2)])

        for i in [2, 3, 4]:
            for j in range(7):
                if self.billes[i][j]:
                    if self.mouvementValide([(i, j), (i + 2, j)]):
                        ListeCoups.append([(i, j), (i + 2, j)])
                    if self.mouvementValide([(i, j), (i - 2, j)]):
                        ListeCoups.append([(i, j), (i - 2, j)])
                    if j < 5:
                        if self.mouvementValide([(i, j), (i, j + 2)]):
                            ListeCoups.append([(i, j), (i, j + 2)])
                    if j > 2:
                        if self.mouvementValide([(i, j), (i, j - 2)]):
                            ListeCoups.append([(i, j), (i, j - 2)])
        return ListeCoups

    def jouerCoup(self, mouv: mouvement):
        nouveauPlateau = Plateau(copy.deepcopy(self.billes))
        if not nouveauPlateau.mouvementValide(mouv):
            raise ValueError("Impossible de jouer un coup non valide.")
        nouveauPlateau.billes[mouv[0][0]][mouv[0][1]] = 0
        nouveauPlateau.billes[(mouv[0][0] + mouv[1][0]) // 2][
            (mouv[0][1] + mouv[1][1]) // 2
        ] = 0
        nouveauPlateau.billes[mouv[1][0]][mouv[1][1]] = 1
        return nouveauPlateau

    def genererVoisins(self):
        ListeVoisins = []
        for coup in self.coupsPossibles():
            ListeVoisins.append(self.jouerCoup(coup))
        return ListeVoisins

    def estValide(self):
        if len(self.billes) != 7:
            raise ValueError("Le plateau n'a pas le bon nombre de lignes.")

        for i in range(7):
            if len(self.billes[i]) != 7:
                raise ValueError("Le plateau n'a pas le bon nombre de colonnes.")

        for i in [0, 1, 5, 6]:
            for j in [2, 3, 4]:
                if self.billes[i][j] != 0 and self.billes[i][j] != 1:
                    raise ValueError("Le plateau ne doit être rempli que de 0 et de 1.")

        for i in [2, 3, 4]:
            for j in range(7):
                if self.billes[i][j] != 0 and self.billes[i][j] != 1:
                    raise ValueError("Le plateau ne doit être rempli que de 0 et de 1.")


# @pyinstrument.profile()
def resoudreSolitaire(plateauInitial: Plateau, plateauFinal: Plateau):
    """
    Résoud le solitaire en utilisant une fonction recursive. On utilise un parcours de graphe en profondeur.
    """
    Chemin: List[Plateau] = []
    Parcourus: List[int] = []
    # CompteurList: List[int] = []

    def explorer(grille: Plateau):
        # print("Compteur : ", CompteurList)
        # CompteurList.append(0)
        print("On a parcouru ", len(Parcourus), " plateaux.")
        """if(len(CompteurList) > 10000):
            return False"""

        print(grille)
        #time.sleep(1)
        # print("Nombre de billes : ", grille.nbBilles())
        Parcourus.append(hash(grille))
        if grille == plateauFinal:
            Chemin.append(grille)
            return True

        for voisin in grille.genererVoisins():
            if (
                hash(voisin) not in Parcourus
                and voisin.nbBilles() >= plateauFinal.nbBilles()
            ):
                if explorer(voisin):
                    Chemin.append(grille)
                    return True
                else:
                    print(grille)
                    #time.sleep(1)
        return False

    # Compteur = 0
    if explorer(plateauInitial):
        for grille in Chemin:
            print(grille)
        return Chemin
    else:
        raise ValueError("Il n'existe pas de solution.")
