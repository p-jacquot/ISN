# Créé par Pierre, le 03/03/2016 en Python 3.2
from math import *
import constantes
from random import *



class Projectile:
    """Classe des projectiles tirés par les atomes."""

    def __init__(self, posX, posY, mv_x, mv_y):
        """Constructeur 'tout simple'..."""
        self.posX = posX
        self.posY = posY
        self.mv_x = mv_x
        self.mv_y = mv_y
        self.dead=False
        self.img = constantes.projectilesList[randint(1,6)].convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY


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
        self.posX += mv_x
        self.posY += mv_y
        self.rect.move_ip(mv_x, mv_y) #On fait bouger le rectangle !
        if self.posY<-20 or self.posY>610 or self.posX[0]<-20 or self.posX>380:
            self.dead=True

