# Créé par Pierre, le 07/03/2016 en Python 3.2
import pygame
pygame.init()
from PIL import Image
from atome import *
from jeu import Jeu
from pattern import *
from random import *




class Molecule:
    """La classe Molécule, qui est un ensemble d'atomes."""

    def __init__(self, atome, posX, posY):
        self.addAtome(atome)
        self.posX = posX
        self.posY = posY
        self.isAlive = True
        #self.mv_x = 0
        #self.mv_y = 0


    def __init__(self, nomMol, pattern):
        self.img = pygame.image.load('resources/photos/'+str(nomMol)).convert_alpha()
        self.rect = self.img.get_rect()
        self.hauteur = self.rect.height
        self.largeur = self.rect.width
        self.atomeList = listerAtomes(nomMol, self.hauteur, self.largeur) #La liste qui contient tous les atomes.
        self.hpMax = vieMol(self.atomeList) #La vie maximale de la molécule, somme de ceux des atomes.
        self.hp = self.hpMax #La vie de la molécule.
        self.posX = 0
        self.posY = 0
        print(self.posX,self.posY,"position origine mol")
        #self.mv_y = 0
        #self.mv_x = 0   #les variables de mouvements.

        self.img = pygame.image.load('resources/photos/'+str(nomMol)).convert_alpha()
        #self.rect = self.img.get_rect()
        self.rectAtome=[]
        for a in self.atomeList:
            a.rect.x=a.posX
            a.rect.y=a.posY
            self.rectAtome.append(a.rect)
        self.rect = self.rectAtome[0].unionall(self.rectAtome[1:])

        self.rectX = self.rect.x  #position du rect dans l'image, il n'est pas en haut à gauche
        self.rectY = self.rect.y

        print(self.rect)
        self.pattern=pattern
        self.dead=False




    def __del__(self):
        del self


    """def addAtome(atome,pos):
        self.atomeList.append(atome)
        self.hpMax += atome.hp
        self.hp = self.hpMax
        self.pos = pos"""

    def move(self):
        """self.posX += self.mv_x
        self.posY += self.mv_y
        self.rect = self.rect.move(self.mv_x, self.mv_y)"""
        self.posX, self.posY = self.pattern.deplacer(self.posX, self.posY)
        self.rect.x = self.posX
        self.rect.y = self.posY

        #TODO: ici, prendre la décision de tirer ou non.
        if self.posX+self.largeur<-50 or self.posX>955 or self.posY+self.hauteur<-50 or self.posY>900:     #changer valeur ici aussi
            self.dead=True   #pas besoin de passer par hit, il n'y aura pas d'animation comme c'est hors de l'écran



    def tirer(self):
        projectiles = []
        for atome in self.atomeList:
            if atome.delayTir<0:
                projectiles+=(atome.tir())
                for a in projectiles:
                    a.posX+=self.posX
                    a.posY+=self.posY
                    a.rect.x=a.posX
                    a.rect.y=a.posY
            else:
                atome.delayTir-=1
        return projectiles

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            print("Aaaaaaaaaah ! Je meurs !")
            self.dead=True


def listerAtomes( nomMol,hauteur,largeur):
        print(nomMol)
        chemin='resources/photos/'+str(nomMol)
        img = Image.open(chemin)

        listeAtomes=[]
        for y in range(hauteur):
            for x in range(largeur):

                pixel = img.getpixel((x,y))

                if pixel==(0,1,0,255) :
                    listeAtomes.append(Carbone(x,y))
                elif pixel == (0,0,1,255):
                    listeAtomes.append(Hydrogene(x,y))
                elif pixel == (1,0,0,255):
                    listeAtomes.append(Oxygene(x,y))
                elif pixel == (0,1,1,255):
                    listeAtomes.append(Azote(x,y))
        return listeAtomes
    #pour tester pour l'instant vous pouvez faire la commande CH4=Molecule('CH4.png')puis print(CH4.atomeList) dans la console


def vieMol(atomeList):
    vie =0
    for a in atomeList :
        vie+=a.hp
    return vie


"""
#Marre que ce code là soit exécuté tout le temps.
Cortizone=Molecule('cortizone.png',500,500,Pattern(0,0))
print(Cortizone.atomeList)
print(Cortizone.hpMax," est la vie max de la cortizone")"""