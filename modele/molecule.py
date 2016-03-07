# Créé par Pierre, le 07/03/2016 en Python 3.2

from atome import *
from model import Modele

class Molecule:
    """La classe Molécule, qui est un ensemble d'atomes."""

    self.atomeList = [] #La liste qui contient tous les atomes.
    self.isAlive = true #Booléen qui rend compte de l'état de la molécule.
    self.hpax #La vie maximale de la molécule, somme de ceux des atomes.
    self.hp #La vie de la molécule.
    self.pos #Tuple de position : (x,y)
    self.mv_y = 0
    self.mv_x = 0   #les variables de mouvements.

    def __init__(self, atome, pos):
        self.addAtome(atome)
        self.pos = pos

    def addAtome(atome):
        self.atomeList.append(atome)
        self.hpMax += atome.hp

    def move():
        pos += (mv_x, mv_y)