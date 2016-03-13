# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

from math import *
from projectiles import Projectile
from pygame.color import *
from pygame.draw import circle
import pygame

class Atome:

    def __init__(self, hp, posX, posY) :
        self.hp=hp
        self.posX = posX
        self.posY = posY

    def Boom(self) :
        print("Boom la molécule explose !")

    def tir(self):
        print("Pew !")
        #Redéfinissez cette fonction dans les classes filles.


class Hydrogene(Atome):

    def __init__(self , hp, posX, posY):
        Atome.__init__(self, hp, posX, posY)
        self.atomeVoisin = None
        #Attention les enfants, ce constructeur ne sert à rien pour l'instant !


    def tir(self, posCible):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        self.modele.add(Projectile(self.position, posCible)) # ce ne sera peut être pas tout à fait la méthode add(), du modèle,

    def seDessiner(self, surface):
        pygame.draw.circle(surface, Color(255, 255, 255, 255), (self.posX, self.posY), 10)

    def lierA(self, atome):
        self.atomeVoisin = atome
        atome.posX = self.posX + 3 # + le rayon
        atome.posY = self.posY
        atome.finirLiaison(self)

    def finirLiaison(self, atomeLie):
        self.atomeVoisin = atomeLie

    """def seLierA(self, atome):
        #Ici c'est l'hydrogène, alors il n'a qu'un seul voisin, mais les autres auront une liste de voisins.
        self.atomeVoisin = atome
        atome.seLierA(self) #Pas sûr de la syntaxe ici."""

class Carbone(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(self, hp, posX, posY)
        self.atomesVoisins = [None, None, None, None] #Dans l'ordre : Droite, Haut, Gauche, Bas.

    def seDessiner(self, surface):
        pygame.draw.circle(surface, Color(0, 0, 0, 255), (self.posX, self.posY), 20)

    def lierA(self, atome, position): #Attention, la position est un nombre entre 0 et 3.
        self.atomesVoisins[position] = atome
        if position == 0:
            atome.posX = self.posX + 20
            atome.posY = self.posY
        elif position == 1:
            atome.posX = self.posX
            atome.posY = self.posY - 20
        elif position == 2:
            atome.posX = self.posX - 20
            atome.posY = self.posY
        elif position == 3:
            atome.posX = self.posX
            atome.posY = self.posY + 20

    def finirLiaison(self, atomeLie, position):
        self.atomesVoisins[position] = atomeLie

class Azote(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(self, hp, posX, posY)
        self.atomesVoisins = [None, None, None] #Dans l'ordre, Droite, haut, gauche.

    def seDessiner(self, surface):
        pygame.draw.circle(surface, Color(0, 0, 255, 255), (self.posX, self.posY), 15)

    def lierA(self, atome, position): #ici, la position est entre 0 et 2.
        """Les positions sont posées assez grossièrement là, mais étant donné qu'on connait le rayon, on pourra améliorer ça plus tard."""
        self.atomesVoisins[position] = atome
        if position == 0:
            atome.posX = self.posX + 5
            atome.posY = self.posY +2
        elif position == 1:
            atome.posX = self.posX
            atome.posY = self.posY - 7

        elif position == 2:
            atome.posX = self.posX -5
            atome.posY = self.posY +2

    def finirLiaison(self, atomeLie, position):
        self.atomesVoisins[position] = atomeLie

class Oxygene(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(self, hp, posX, posY)
        self.atomesVoisins = [None, None] #Dans l'ordre : Gauche, Droite.

    def seDessiner(self, surface):
        pygame.draw.circle(surface, Color(255, 0, 0, 255), (self.posX, self.posY), 12)

    def lierA(self, atome, position): # De 0 à 1
        self.atomesVoisins[position] = atome
        if position == 0:
            atome.posX = self.posX + 5
            atome.posY = self.posY
        elif position == 1:
            atome.posX = self.posX -5
            atome.posY = self.posY

    def finirLiaison(self, atomeLie, position):
        self.atomesVoisins[position] = atomeLie