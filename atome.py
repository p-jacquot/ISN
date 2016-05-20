# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2
import pygame
pygame.init()
from math import *
from projectiles import *
from random import *

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
        self.delayTirMax=500
        self.delayTir=randint(0,self.delayTirMax)
        img = pygame.image.load('resources/photos/hydrogene.png').convert_alpha()
        self.rect = img.get_rect()
        self.compteur = 0
        self.cible = randint ( -3,3)

    def tir(self):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        if self.compteur == 5 :
            self.delayTir=self.delayTirMax
            self.compteur = 0
            self.cible = randint ( -3,3)
        else :
            self.compteur += 1
            self.delayTir = 30
            return [Projectile(self.posX,self.posY ,self.cible/5, 0.5 )]
        """x1, y1 = 0, 0
        #x2, y2 = jeu.moleculeJoueur.posX,jeu.moleculeJoueur.posY
        x2,y2=200,300
        distance=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        a = float((x2-x1)/distance)
        b = float((y2-y1)/distance)
        return [Projectile(self.posX, self.posY, int(a*2), int(b*2))]"""
        return []


class Carbone(Atome):

    def __init__(self, posX, posY):
        Atome.__init__(self,  posX, posY)
        self.tirNum = -1
        self.hp=150
        self.delayTirMax=250
        self.delayTir=randint(0,self.delayTirMax)
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
        self.delayTirMax=75
        self.delayTir=randint(0,self.delayTirMax)
        self.angle=10
        img = pygame.image.load('resources/photos/oxygene.png').convert_alpha()
        self.rect = img.get_rect()


    def tir(self):
        #self.angle = #angle entre chaques tirs
        self.tirNum += 0.02
        self.delayTir=self.delayTirMax
        return [Projectile(self.posX, self.posY, cos((self.angle*self.tirNum))*pi/5, sin((self.angle*self.tirNum))*pi/5)]

class Azote(Atome):

    def __init__(self,posX,posY):
        Atome.__init__(self,posX,posY)
        self.hp=30
        self.delayTirMax=350
        self.delayTir=randint(0,self.delayTirMax)
        img = pygame.image.load('resources/photos/azote.png').convert_alpha()
        self.rect = img.get_rect()

    def tir(self):
        self.delayTir=self.delayTirMax
        return[Projectile(self.posX,self.posY, 0,1),Projectile(self.posX,self.posY,0.5,1),Projectile(self.posX,self.posY,-0.5,1)]


class Chlore(Atome):

    def __init__(self , posX, posY):
        Atome.__init__(self,  posX, posY)
        self.hp=30
        self.delayTirMax=1000
        self.delayTir=randint(0,self.delayTirMax)
        img = pygame.image.load('resources/photos/chlore.png').convert_alpha()
        self.rect = img.get_rect()
        self.compteur = 0


    def tir(self):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        if self.compteur == 30 :
            self.delayTir=self.delayTirMax
            self.compteur = 0

        else :
            self.cible = randint ( -3,3)
            self.compteur += 1
            self.delayTir = 1
            return [Projectile(self.posX,self.posY ,self.cible/100, 0.15 )]
        return []

class Soufre(Atome):

    def __init__(self,posX,posY):
        Atome.__init__(self,posX,posY)
        self.hp=50
        self.delayTirMax=1000
        self.delayTir=randint(500,self.delayTirMax)
        img = pygame.image.load('resources/photos/soufre.png').convert_alpha()
        self.rect = img.get_rect()

    def tir(self):
        self.delayTir=self.delayTirMax
        return [Laser(self.posX,self.posY, 0,1,0,0),Laser(self.posX,self.posY,0.5,0.5,45,0),Laser(self.posX,self.posY,-0.5,0.5,45,0)]


class Boson(Atome):

    def __init__(self,posX,posY):
        Atome.__init__(self,posX,posY)
        self.hp=5000
        self.delayTirMax=100
        self.delayTir=1
        img = pygame.image.load('resources/photos/boson.png').convert_alpha()
        self.rect = img.get_rect()
        self.attaque = 0
        self.tirprojectiles= 0
        self.tirlasers= 0
        self.tirbashp= 0

    def tir(self):
        self.attaque = randint(1,5)
        if self.attaque == 1 and self.tirprojectiles==0 and self.tirlasers==0 and self.tirbashp==0:
            self.delayTir = self.delayTirMax
            return [Laser(self.posX,self.posY, 0,1,0,2),Laser(self.posX,self.posY,0.5,0.5,45,2),Laser(self.posX,self.posY,-0.5,0.5,45,2),Laser(self.posX,self.posY, -0.5,-0.5,0,2),Laser(self.posX,self.posY,0.5,-0.5,45,2),Laser(self.posX,self.posY,0,-1,45,2),Laser(self.posX,self.posY, 1,0,0,2),Laser(self.posX,self.posY,-1,0,45,2)]
        elif (self.attaque == 2 or self.tirprojectiles>0) and self.tirlasers==0 and self.tirbashp==0:
            if self.tirprojectiles<50:
                directiontir = randint(-100,100)
                self.tirprojectiles += 1
                self.delayTir = 1
                return [Projectile(self.posX,self.posY,directiontir/100,1)]
            elif self.tirprojectiles>=50:
                self.delayTir = 200
                self.tirprojectiles = 0
            return []
        elif (self.attaque == 3 or self.tirlasers>0) and self.tirprojectiles==0 and self.tirbashp==0:
            if self.tirlasers<10:
                directiontir = randint(-100,100)
                self.tirlasers += 1
                self.delayTir = 1
                return [Laser(self.posX,self.posY,directiontir/100,1,45,2)]
            elif self.tirlasers>=10:
                self.delayTir = 1000
                self.tirlasers = 0
            return []
        elif self.attaque == 4 and self.tirprojectiles==0 and self.tirlasers==0 and self.tirbashp==0:
            self.delayTir= 500
            return []
        elif (self.attaque == 5 or self.tirbashp>0) and self.tirprojectiles==0 and self.tirlasers==0:
            if self.tirbashp<500:
                directiontir = randint(-20,20)
                self.tirbashp += 1
                self.delayTir = 1
                return [Projectile(self.posX,self.posY,directiontir/100,0.1)]
            elif self.tirbashp>=500:
                self.delayTir= self.delayTirMax
                self.tirbashp=0
            return []
