# Créé par Pierre, le 03/03/2016 en Python 3.2
from math import *

class Projectile:
    """Classe des projectiles tirés par les atomes."""

    def __init__(self, pos, mv):
        """Constructeur 'tout simple'..."""
        self.position = [pos[0],pos[1]] #tuple de position.
        self.mouvement = [mv[0],mv[1]] #liste de mouvement.
        self.dead=False

    """ def __init__(self, pos, posCible,equipe):
        #Le fameux constructeur qui va permettre de viser le joueur.
        self.position = pos
        x1, y1 = pos
        x2, y2 = posCible
        #a = int((y2-y1)/(x2-x1))
        #b = y1 - a*x1
        distance=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        #on calcule le module et presque l'argument du vecteur atome cible
        a = (x2-x1)/distance
        b = (y2-y1)/distance
        self.mouvement = (a,b)"""

    def move(self):
        self.position[0]+=self.mouvement[0]
        self.position[1]+=self.mouvement[1]
        if self.position[1]<-20 or self.position[1]>610 or self.position[0]<-20 or self.position[0]>380:
            self.dead=True

