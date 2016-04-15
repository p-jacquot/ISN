# Créé par Pierre, le 03/03/2016 en Python 3.2
from math import *
import constantes
<<<<<<< HEAD
from random import *

=======
>>>>>>> 7c48705d2dd2eb653406e84dd764d749d901ccf4

class Projectile:
    """Classe des projectiles tirés par les atomes."""

    def __init__(self, posX, posY, mv_x, mv_y):
        """Constructeur 'tout simple'..."""
        self.posX = posX
        self.posY = posY
        self.mv_x = mv_x
        self.mv_y = mv_y
        self.dead=False
<<<<<<< HEAD
        self.img = projectilesList[randint(1,6)].convert_alpha()
        self.rect = self.img.get_rect()
=======
        self.img = constantes.projectilesList[0] #on pourra y mettre un random entre 0 et 6, si vous voulez.
        self.rect = img.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

>>>>>>> 7c48705d2dd2eb653406e84dd764d749d901ccf4
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

