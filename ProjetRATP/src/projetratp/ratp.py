from typing import Tuple

class Gare(object):

    def __init__(self, nom:str, id:int, coord:Tuple[float,float]):
        self.nom:str = nom
        self.id:int = id
        self.x:float = coord[0]
        self.y:float = coord[1]

    def __str__(self):
        return "Nom : "+self.nom + "\n Lon. "+str(self.x)+" Lat. "+str(self.y)
