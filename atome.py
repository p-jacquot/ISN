# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2
import pygame
pygame.init()
from math import *
from projectiles import Projectile

class Atome:

    def __init__(self,  posX, posY) :

        self.posX = posX
        self.posY = posY


    def Boom(self) :
        print("Boom la molécule explose !")
        self.__del__()

    def tir(self):
        print("Pew !")
        #Redéfinissez cette fonction dans les classes filles.
    def __del__(self):
        pass    #ça, ça sert à rien, je pense.


class Hydrogene(Atome):

    def __init__(self , posX, posY):
        Atome.__init__(self,  posX, posY)
        self.hp=10
        self.delayTirMax=50
        self.delayTir=self.delayTirMax
        img = pygame.image.load('resources/photos/hydrogene.png').convert_alpha()
        self.rect = img.get_rect()

    def tir(self):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        self.delayTir=self.delayTirMax

        x1, y1 = self.posX,self.posY
        #x2, y2 = jeu.moleculeJoueur.posX,jeu.moleculeJoueur.posY
        x2,y2=100,100
        distance=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        a = int((x2-x1)/distance)
        b = int((y2-y1)/distance)
        #return [Projectile(self.posX, self.posY, a, b)]
        return []


class Carbone(Atome):

    def __init__(self, posX, posY):
        Atome.__init__(self,  posX, posY)
        self.tirNum = -1
        self.hp=150
        self.delayTirMax=150
        self.delayTir=self.delayTirMax
        img = pygame.image.load('resources/photos/carbone.png').convert_alpha()
        self.rect = img.get_rect()


    def tir(self):
        self.tirNum = -self.tirNum
        self.delayTir=self.delayTirMax
        if self.tirNum == -1:
            return [Projectile(self.posX, self.posY, -1, 0), Projectile(self.posX, self.posY, 1, 0), Projectile(self.posX, self.posY, 0, 1), Projectile(self.posX, self.posY, 0, -1)]
        elif self.tirNum == 1:
            return [Projectile(self.posX, self.posY, -1, -1), Projectile(self.posX, self.posY, 1, -1), Projectile(self.posX, self.posY, 1, 1), Projectile(self.posX, self.posY, -1, 1)]

class Oxygene(Atome):

    def __init__(self, posX, posY):
        Atome.__init__(self, posX, posY)
        self.tirNum = 0
        self.hp=20
        self.delayTirMax=30
        self.delayTir=self.delayTirMax
        self.angle=0
        img = pygame.image.load('resources/photos/oxygene.png').convert_alpha()
        self.rect = img.get_rect()


    def tir(self):
        #self.angle = #angle entre chaques tirs
        self.tirNum += 1
        self.delayTir=self.delayTirMax
        #return [Projectile(self.posX, self.posY, cos((self.angle*self.tirNum))/60*pi, sin((self.angle*self.tirNum))/60*pi)]
        return []

class Azote(Atome):

    def __init__(self,posX,posY):
        Atome.__init__(self,posX,posY)
        self.hp=30
        self.delayTirMax=100
        self.delayTir=self.delayTirMax
        img = pygame.image.load('resources/photos/azote.png').convert_alpha()
        self.rect = img.get_rect()

    def tir(self):
        self.delayTir=self.delayTirMax
        return[Projectile(self.posX,self.posY, 0,2),Projectile(self.posX,self.posY,1,2),Projectile(self.posX,self.posY,-1,2)]


