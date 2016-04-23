# Créé par Pierre, le 05/03/2016 en Python 3.2
from PIL import Image

import random
from dialogue import Dialog
from molecule import Molecule
from pattern import Pattern
import copy

class Niveau:
    """La classe qui gère les niveaux."""

    """def __init__(self, mobOnScreen, totalMob):
        self.mobList = [] #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        self.maxMobOnScreen = mobOnScreen #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLeft = totalMob"""

    def __init__(self, numero, firstDialog, middleDialog, lastDialog):

        self.fname=str("resources/niveau/"+str(numero)+"/mobs.txt")
        self.pathMusicLevel = str("resources/niveau/" + str(numero) + "/music.wav")
        self.pathMusicBoss = str("resources/niveau/" + str(numero) + "/musicBoss.wav")
        self.mobList = [] #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        with open(self.fname) as text:
            content = text.readlines()
        self.boss = Molecule(str(content[0][:-1]), Pattern(0,0))
        for a in content[1:-2]:
            self.mobList.append([Molecule(str(a[:-4]), Pattern(0, 1)), int(a[-3:-1])])
        self.maxMobOnScreen = int(content[-2]) #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLeft = int(content[-1])
        self.firstDialog = firstDialog  #Les différents dialogues qu'ils y aura dans le niveau.
        self.middleDialog = middleDialog
        self.lastDialog = lastDialog


    def genererMob(self):
        rand = random.randint(0, 99)
        #print(rand)
        ennemi = None
        for mob in self.mobList:
            if rand <= mob[1]:
                #code en attendant de sérialiser les molécules
                """name = "resources/photos/"+str(mob[0])
                img=Image.open(name)
                taille=img.size
                pattern=Pattern(0,0)"""
                self.totalMobsLeft -= 1
                ennemi = copy.deepcopy(mob[0])
                ennemi.img =mob[0].img
                ennemi.posY = 5
                ennemi.posX = random.randint(0, 350)
                ennemi.rect.x = ennemi.posX
                ennemi.rect.y = ennemi.posY
                #print("Apparition aux coordonnées :", ennemi.posX, ",", ennemi.posY)
                #print("Son rect est :", ennemi.rect)
                #print("--------------------------------------")
                """rand=random.randint(1,3)
                if rand== 1 :#en haut
                    ennemi.posY= -5
                    ennemi.posX=random.randint(-5,350)
                    print("En haut !")
                else:
                    ennemi.posY=random.randint(-5,350)#je pense pas que le jeu fasse la largeur de l'écran alors il faudra changer cette valeur quand on saura
                    if rand==2:
                        print("Heu... Sur la gauche ?")
                        ennemi.posX=-5
                    else :
                        ennemi.posX=350#idem ici
                        print("Sur la droite, je pense.")"""
                break
        return ennemi

    #TODO: Rajouter une fonction __repr__() pour qu'on puisse voir clairement un niveau, et l'éditer s'il le faut.


