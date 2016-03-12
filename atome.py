# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

from math import *
from projectiles import Projectile
from pygame.color import *
from pygame.draw import circle

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
        Atome.__init__(hp, posX, posY)
        self.atomeVoisin = None
        #Attention les enfants, ce constructeur ne sert à rien pour l'instant !


    def tir(self, posCible):
        #distanceCible = int(sqrt(pow(xCible-self.x,2)+pow(yCible-self.y,2)))
        #print(distanceCible)
        self.modele.add(Projectile(self.position, posCible)) # ce ne sera peut être pas tout à fait la méthode add(), du modèle,

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, WHITE, (posX, posY), 3)

    def lierA(self, atome):
        self.atomeVoisin = atome
        atome.posX = self.posX + 3 # + le rayon
        atome.posY = self.posY

    """def seLierA(self, atome):
        #Ici c'est l'hydrogène, alors il n'a qu'un seul voisin, mais les autres auront une liste de voisins.
        self.atomeVoisin = atome
        atome.seLierA(self) #Pas sûr de la syntaxe ici."""

class Carbone(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(hp, posX, posY)
        self.atomesVoisins = [None, None, None, None] #Dans l'ordre : Droite, Haut, Gauche, Bas.

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, BLACK, (posX, posY), 10)

    def lierA(self, atome, position): #Attention, la position est un nombre entre 0 et 3.
        self.atomesVoisins[position] = atome
        if position == 0:
            atome.posX = self.posX + 10
            atome.posY = self.posY
        elif position == 1:
            atome.posX = self.posX
            atome.posY = self.posY - 10
        elif position == 2:
            atome.posX = self.posX - 10
            atome.posY = self.posY
        elif position == 3:
            atome.posX = self.posX
            atome.posY = self.posY + 10


class Azote(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(hp, posX, posY)
        self.atomesVoisins = [None, None, None] #Dans l'ordre, Droite, haut, gauche.

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, BLUE, (posX, posY), 7)

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

class Oxygene(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(hp, posX, posY)
        self.atomesVoisins = [None, None] #Dans l'ordre : Gauche, Droite.

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, RED, (posX, posY), 5)

    def lierA(self, atome, position): # De 0 à 1
        self.atomesVoisins[position] = atome
        if position == 0:
            atome.posX = self.posX + 5
            atome.posY = self.posY
        elif position == 1:
            atome.posX = self.posX -5
            atome.posY = self.posY