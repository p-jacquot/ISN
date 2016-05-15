# Créé par Pierre, le 03/03/2016 en Python 3.2
from math import *
import constantes
from random import *
import pygame


class Projectile:
    """Classe des projectiles tirés par les atomes."""

    def __init__(self, posX, posY, mv_x, mv_y):
        """Constructeur 'tout simple'..."""
        self.posX = posX
        self.posY = posY
        self.mv_x = mv_x*8
        self.mv_y = mv_y*8
        self.dead=False
        self.img = constantes.projectilesList[randint(1,6)].convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY
    def __del__(self):
        del self

    """    def __init__(self, posX, posY, mv_x, mv_y, indexImg):
        #Constructeur quasi identique, mais on peut choisir l'image du projectile. (pour ceux du joueur, ce sera tous les mêmes)
        self.posX = posX
        self.posY = posY
        self.mv_x = mv_x
        self.mv_y = mv_y
        self.dead=False
        self.img = constantes.projectilesList[indexImg].convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY"""

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
        self.posX += self.mv_x
        self.posY += self.mv_y
        self.rect.x = self.posX
        self.rect.y = self.posY
        #self.rect.move_ip(self.mv_x, self.mv_y) #On fait bouger le rectangle !
        if self.posY<-20 or self.posY>constantes.hauteur+20 or self.posX<-20 or self.posX>constantes.largeur+20:
            self.dead=True


class Laser:                                                            #Ne fait pas encore de rotation a l'image du laser, du coup c'est moche

    def __init__(self, posX, posY, mv_x, mv_y,rtImg,rebond):
        self.posX = posX
        self.posY = posY
        self.mv_x = mv_x*6
        self.mv_y = mv_y*6
        self.rtImg = rtImg
        self.rebond = rebond
        self.dead=False
        self.img= constantes.laser.convert_alpha()
        self.imgrt= pygame.transform.rotate(self.img,self.rtImg)
        self.rect = self.img.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

    def __del__(self):
        del self

    def move(self):
        self.posX += self.mv_x
        self.posY += self.mv_y
        self.rect.x = self.posX
        self.rect.y = self.posY
        if self.posX<=0 or self.posX>=constantes.largeur and self.rebond<5:
            self.rebond += 1
            self.mv_x = -self.mv_x
            self.mv_y = self.mv_y
            self.rtImg =acos(self.mv_y/(sqrt(pow(self.mv_x,2)+pow(self.mv_y,2))))

        if self.posY<=0 or self.posY>=constantes.hauteur and self.rebond<5:
            self.rebond = self.rebond+1
            self.mv_x=self.mv_x
            self.mv_y=-self.mv_y
            self.rtImg = acos(self.mv_x/(sqrt(pow(self.mv_x,2)+pow(self.mv_y,2))))
        if self.posY<-20 or self.posY>constantes.hauteur+20 or self.posX<-20 or self.posX>constantes.largeur+20:
                self.dead=True
