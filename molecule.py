# Créé par Pierre, le 07/03/2016 en Python 3.2
from PIL import Image
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


    def __init__(self,nomMol):
        self.atomeList = listerAtomes(nomMol) #La liste qui contient tous les atomes.
        #self.isAlive = true #Booléen qui rend compte de l'état de la molécule.  #Pour l'instant je l'ai viré parce qu'il faisait une erreur
        self.hpMax = 0 #La vie maximale de la molécule, somme de ceux des atomes.
        self.hp = 0 #La vie de la molécule.
        self.pos = (0,0) #Tuple de position : (x,y)
        self.mv_y = 0
        self.mv_x = 0   #les variables de mouvements.


    def addAtome(atome,pos):
        self.atomeList.append(atome)
        self.hpMax += atome.hp
        self.hp = self.hpMax
        self.pos = pos

    def move():
        pos += (mv_x, mv_y)
        #TODO: ici, prendre la décision de tirer ou non.


def listerAtomes( nomMol):
        img = Image.open(nomMol)
        listeAtomes=[]
        for y in range(250):
            for x in range(250):
                pixel = img.getpixel((x,y))
                if pixel==(220,220,220,255) :
                    listeAtomes.append(('C',(x,y)))
                elif pixel == (200,178,178,255):
                    listeAtomes.append(('H',(x,y)))
        return listeAtomes
    #pour tester pour l'instant vous pouvez faire la commande CH4=Molecule('CH4.png')puis print(CH4.atomeList) dans la console
CH4=Molecule('CH4.png')
print(CH4.atomeList)