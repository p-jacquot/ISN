# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

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
    def tir(self, posCible):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        self.modele.add(Projectile((self.posX, self.posY), posCible,0 )) # ce ne sera peut être pas tout à fait la méthode add(), du modèle,
        #le troisieme argument est pour différencier d'où vient le projectile (0=ennemi,1=joueur) et aussi pour différencier les deux constructeurs de l'autre coté

class Carbone(Atome):

    def __init__(self, posX, posY):
        Atome.__init__(self,  posX, posY)
        self.tirNum = -1
        self.hp=40

    def tir(self):
        if self.tirNum == -1:
            return [Projectile((self.posX, self.posY), (-1, 0)), Projectile((self.posX, self.posY), (1, 0)), Projectile((self.posX, self.posY), (0, 1)), Projectile((self.posX, self.posY), (0, -1))]
        elif self.tirNum == 1:
            return [Projectile((self.posX, self.posY), (-1, -1)), Projectile((self.posX, self.posY), (1, -1)), Projectile((self.posX, self.posY), (1, 1)), Projectile((self.posX, self.posY), (-1, 1))]
        tirNum = -tirNum

class Oxygene(Atome):

    def __init__(self, posX, posY):
        Atome.__init__(self, posX, posY)
        self.tirNum = 0
        self.hp=20

    def tir(self):
        #self.angle = #angle entre chaques tirs
        return [Projectile((self.posX, self.posY), (cos((self.angle*self.tirNum)/180*pi), sin((self.angle*self.tirNum))/180*pi))]
        tirNum += 1


class Azote(Atome):

    def __init__(self,posX,posY):
        Atome.__init__(self,posX,posY)
        self.hp=30

    def tir(self):
        return[Projectile((self.posX,self.posY),(0,2)),Projectile((self.posX,self.posY),(1,2)),Projectile((self.posX,self.posY),(-1,2))]


