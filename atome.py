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

    """def seLierA(self, atome):
        #Ici c'est l'hydrogène, alors il n'a qu'un seul voisin, mais les autres auront une liste de voisins.
        self.atomeVoisin = atome
        atome.seLierA(self) #Pas sûr de la syntaxe ici."""

class Carbone(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(hp, posX, posY)
        self.atomeVoisinHaut = None
        self.atomeVoisinBas = None
        self.atomeVoisinGauche = None
        self.atomeVoisinDroite = None

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, BLACK, (posX, posY), 10)

class Azote(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(hp, posX, posY)
        self.atomeVoisinHaut = None
        self.atomeVoisinDroit = None
        self.atomeVoisinGauche = None

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, BLUE, (posX, posY), 7)

class Oxygene(Atome):

    def __init__(self, hp, posX, posY):
        Atome.__init__(hp, posX, posY)
        self.atomeVoisinDroit = None
        self.atomeVoisinGauche = None

    def seDessiner(self, surface):
        Pygame.draw.circle(surface, RED, (posX, posY), 5)