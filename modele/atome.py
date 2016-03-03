# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

from math import *
from projectiles import Projectile

class Atome:

    def __init__(self, hp, pos, modele) :
        self.hp=hp
        self.position = pos #pos : tuple de la forme (positionX, positionY)
        self.modele = modele

    def Boom(self) :
        print("Boom la molécule explose !")

    def tir(self):
        print("Pew !")
        #Redéfinissez cette fonction dans les classes filles.


class Hydrogene(Atome):

    def __init__(self , hp, pos, modele):
        Atome.__init__(hp, pos, modele)
        #Attention les enfants, ce constructeur ne sert à rien pour l'instant !


    def tir(self, posCible):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        self.modele.add(Projectile(self.position, posCible)) # ce ne sera peut être pas tout à fait la méthode add(), du modèle,