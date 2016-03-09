# Créé par Pierre, le 07/03/2016 en Python 3.2

from atome import *
from modele import Modele

class Molecule:
    """La classe Molécule, qui est un ensemble d'atomes."""

    def __init__(self, atome, pos):
        self.addAtome(atome)
        self.pos = pos
        self.isAlive = True
        self.mv_x = 0
        self.mv_y = 0

    def __init__(self):
        self.atomeList = [] #La liste qui contient tous les atomes.
        self.isAlive = true #Booléen qui rend compte de l'état de la molécule.
        self.hpMax = 0 #La vie maximale de la molécule, somme de ceux des atomes.
        self.hp = 0 #La vie de la molécule.
        self.pos = (0,0) #Tuple de position : (x,y)
        self.mv_y = 0
        self.mv_x = 0   #les variables de mouvements.

    def addAtome(atome):
        self.atomeList.append(atome)
        self.hpMax += atome.hp
        self.hp = self.hpMax

    def move():
        pos += (mv_x, mv_y)
        #TODO: ici, prendre la décision de tirer ou non.