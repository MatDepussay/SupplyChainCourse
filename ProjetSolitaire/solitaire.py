
type mouvement = List[Tuple[int]]

class Plateau(object):

    def __init__(self, grille):
        self.billes = grille #0 -> Pas de bille, 1 -> une bille
        self.estValide()

    def __eq__(self, autrePlateau) -> bool: # MonPlateau == AutrePlateau ?
        for i in [0,1,5,6]:
            for j in [2,3,4]:
                if self.billes[i][j] != autrePlateau.billes[i][j]:
                    return False

        for i in [2,3,4]:
            for j in range(7):
                if self.billes[i][j] != autrePlateau.billes[i][j]:
                    return False
        return True

    def mouvementValide(self, mouv:mouvement): #mouv = [(x,y), (x,y)]

        #Verifier case arrivee vide :
        if self.billes[ mouv[1][0] ][ mouv[1][1] ] != 0:
            return False

        #Verifier horizontal ou vertical
        if mouv[0][0] != mouv[1][0] and mouv[0][1] != mouv[1][1]:
            return False

        #Verifier case de depart
        if self.billes[ mouv[0][0] ][ mouv[0][1] ] == 0:
            return False

        #Verifier case du milieu
        if self.billes[ (mouv[0][0] + mouv[1][0]) // 2 ][ (mouv[0][1] + mouv[1][1]) // 2  ] == 0:
            return False

        #Verifier saut de 2
        if abs(mouv[0][0] - mouv[1][0]) != 2 and  abs(mouv[0][1] - mouv[1][1]) !=2:
            return False

        #Verifier cases dans le plateau
        if mouv[0][0] in [0,1,5,6]:
            if mouv[0][1] not in [2,3,4]:
                    return False

        if mouv[1][0] in [0,1,5,6]:
            if mouv[1][1] not in [2,3,4]:
                    return False

        return True

    def estValide(self):
        if(len(self.billes) != 7):
            raise ValueError("Le plateau n'a pas le bon nombre de lignes.")

        for i in range(7):
            if(len(self.billes[i]) != 7):
                raise ValueError("Le plateau n'a pas le bon nombre de colonnes.")

        for i in [0,1,5,6]:
            for j in [2,3,4]:
                if self.billes[i][j] != 0 and self.billes[i][j] != 1:
                    raise ValueError("Le plateau ne doit être rempli que de 0 et de 1.")

        for i in [2,3,4]:
            for j in range(7):
                if self.billes[i][j] != 0 and self.billes[i][j] != 1:
                    raise ValueError("Le plateau ne doit être rempli que de 0 et de 1.")
