# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

from math import *

class Atome:

    def __init__(self, hp, pos) :
        self.hp=hp
        self.position = pos

    def Boom(self) :
        print("Boom la molécule explose !")

    def tir(self):
        print("Pew !")
        #Redéfinissez cette fonction dans les classes filles.


class Hydrogene(Atome):

    def __init__(self , hp, pos):
        Atome.__init__(hp, pos)
        #Attention les enfants, ce constructeur ne sert à rien pour l'instant !


    def tir(self,xCible,yCible):
        distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        print(distanceCible)