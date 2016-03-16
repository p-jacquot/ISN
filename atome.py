# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

from math import *
from projectiles import Projectile

class Atome:

    def __init__(self, hp, pos) :
        self.hp = hp
        self.position = pos #pos : tuple de la forme (positionX, positionY)

    def Boom(self) :
        print("Boom la molécule explose !")
        self.__del__()

    def tir(self):
        print("Pew !")
        #Redéfinissez cette fonction dans les classes filles.
    def __del__(self):
        pass    #ça, ça sert à rien, je pense.


class Hydrogene(Atome):

    def __init__(self , hp, pos):
        Atome.__init__(self, hp, pos)
        self.atomeVoisin = True
        #Attention les enfants, ce constructeur ne sert à rien pour l'instant !

    def tir(self, posCible):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        self.modele.add(Projectile(self.position, posCible,0 )) # ce ne sera peut être pas tout à fait la méthode add(), du modèle,
        #le troisieme argument est pour différencier d'où vient le projectile (0=ennemi,1=joueur) et aussi pour différencier les deux constructeurs de l'autre coté

    def seLierA(self, atome):
        #Ici c'est l'hydrogène, alors il n'a qu'un seul voisin, mais les autres auront une liste de voisins.
        self.atomeVoisin = atome
        atome.seLierA(self) #Pas sûr de la syntaxe ici.

class Carbone(Atome):

    def __init__(self,hp,pos,modele):
        Atome.__init__(self,hp,pos,modele)
        self.tirNum = -1

    def tir():
        if self.tirNum == -1:
            return [Projectile(self.position, (-1, 0)), Projectile(self.position, (1, 0)), Projectile(self.position, (0, 1)), Projectile(self.position, (0, -1))]
        elif self.tirNum == 1:
            return [Projectile(self.position, (-1, -1)), Projectile(self.position, (1, -1)), Projectile(self.position, (1, 1)), Projectile(self.position, (-1, 1))]
        tirNum = -tirNum

class Oxygene(Atome):
    def __init__(self, hp, pos, modele):
        Atome.__init__(self, hp, pos, modele)
        self.tirNum = 0
    def tir(self, angle):
        self.angle = angle #angle entre chaques tirs
        return [Projectile(self.position, (cos((self.angle*self.tirNum)/180*pi), sin((self.angle*self.tirNum))/180*pi))]
        tirNum += 1


