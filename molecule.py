# Créé par Pierre, le 07/03/2016 en Python 3.2
#from PIL import Image
from atome import *
from modele import Modele
import pygame
import pygame.rect



class Molecule:
    """La classe Molécule, qui est un ensemble d'atomes."""

    def __init__(self, atomeList, posX, posY):
        self.atomeList = atomeList
        self.posX = posX
        self.posY = posY
        self.isAlive = True
        self.mv_x = 0
        self.mv_y = 0
        self.hp = 0
        self.hpMax = 0
        self.countHP()
        self.surface = None


    """def __init__(self, nomMol, hauteur, largeur):
        self.atomeList = listerAtomes(nomMol,hauteur,largeur) #La liste qui contient tous les atomes.
        #self.isAlive = true #Booléen qui rend compte de l'état de la molécule.  #Pour l'instant je l'ai viré parce qu'il faisait une erreur
        self.hpMax = vieMol(self.atomeList) #La vie maximale de la molécule, somme de ceux des atomes.
        self.hp = 0 #La vie de la molécule.
        self.pos = (0,0) #Tuple de position : (x,y)
        self.mv_y = 0
        self.mv_x = 0   #les variables de mouvements."""


    """def addAtome(atome,pos):
        self.atomeList.append(atome)
        self.hpMax += atome.hp
        self.hp = self.hpMax
        self.pos = pos"""

    def move(self):
        self.posX += self.mv_x
        self.posY += self.mv_y
        #TODO: ici, prendre la décision de tirer ou non.

    def countHP(self):
        for atome in self.atomeList:
            self.hpMax += atome.hp
        self.hp = self.hpMax

    def seDessiner(self):
        x_max = 0
        y_max = 0
        x_min = 1000
        y_min = 1000
        for atome in self.atomeList:
            if atome.posX - atome.rayon < x_min:
                x_min = atome.posX - atome.rayon
            if atome.posY - atome.rayon < y_min:
                y_min = atome.posY - atome.rayon
        for atome in self.atomeList:
            atome.posX -= x_min
            atome.posY -= y_min
        for atome in self.atomeList:
            if atome.posX + atome.rayon > x_max:
                x_max = atome.posX+atome.rayon
            if atome.posY + atome.rayon> y_max:
                y_max = atome.posY + atome.rayon
        surface = pygame.display.set_mode((x_max, y_max))
        pygame.draw.rect(surface, Color(100, 100, 100), (0, 0, x_max, y_max))
        for atome in self.atomeList:
            atome.seDessiner(surface)

        self.surface = surface
        pygame.image.save(surface, 'test.png')


"""def listerAtomes( nomMol,hauteur,largeur):
        img = Image.open(nomMol)
        listeAtomes=[]
        for y in range(hauteur):
            for x in range(largeur):

                pixel = img.getpixel((x,y))

                if pixel==(0,1,0,255) :
                    listeAtomes.append(('C',(x,y)))
                elif pixel == (0,0,1,255):
                    listeAtomes.append(('H',(x,y)))
                elif pixel == (1,0,0,255):
                    listeAtomes.append(('O',(x,y)))
                elif pixel == (0,1,1,255):
                    listeAtomes.append(('N',(x,y)))
        return listeAtomes
    #pour tester pour l'instant vous pouvez faire la commande CH4=Molecule('CH4.png')puis print(CH4.atomeList) dans la console"""


"""def vieMol(atomeList):
    vie =0
    for a in atomeList :
        if a[0]=='H':
            vie+=10
        elif a[0]=='C':
            vie+=40
        elif a[0]=='O':
            vie+=20
        elif a[0]=='N':
            vie+=30
    return vie
Cortizone=Molecule('resources/photos/cortizone.png',500,500)
print(Cortizone.atomeList)
print(Cortizone.hpMax," est la vie max de la cortizone")"""

if __name__ == "__main__":
    pygame.init()
    carb = Carbone(10, 50, 50)
    azo = Azote(7, 0, 0)
    hydr = Hydrogene(2, 0, 0)
    carb.lierA(azo, 3)
    carb.lierA(azo, 1)
    carb.lierA(azo, 0)
    azo.finirLiaison(carb, 0)
    azo.finirLiaison(carb, 1)
    azo.finirLiaison(carb, 2)
    carb.lierA(hydr, 2)
    hydr.finirLiaison(carb)
    mol = Molecule([carb, azo, hydr], 0, 0)
    #scrn = pygame.display.set_mode((100, 100))
    mol.seDessiner()
    pygame.quit()