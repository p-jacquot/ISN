# Créé par Pierre, le 05/03/2016 en Python 3.2
from PIL import Image

from random import *
from dialogue import Dialog
from molecule import Molecule
import copy
import constantes
from pattern import *
import pickle

class Niveau:
    """La classe qui gère les niveaux."""

    """def __init__(self, mobOnScreen, totalMob):
        self.mobList = [] #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        self.maxMobOnScreen = mobOnScreen #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLeft = totalMob"""

    def __init__(self, numero):
        self.numero=numero
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

        with open("resources/niveau/"+str(numero)+"/firstDialog.pickle", 'rb') as file:
            firstDialog = pickle.load(file)
        with open("resources/niveau/"+str(numero)+"/middleDialog.pickle", 'rb') as file:
            middleDialog = pickle.load(file)
        with open(str("resources/niveau/"+str(numero)+"/lastDialog.pickle"), 'rb') as file:
            lastDialog = pickle.load(file)

        self.firstDialog = firstDialog  #Les différents dialogues qu'ils y aura dans le niveau.
        self.middleDialog = middleDialog
        self.lastDialog = lastDialog


    def genererMob(self):
        rand =  randint(0, 99)
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



                randomPattern= randint(0,4)

                if randomPattern == 0 : #pattern normal
                    ennemi.pattern = Pattern(randint(-1,1),1)
                    ennemi.posY = 5
                    ennemi.posX =  randint(0, constantes.largeur-ennemi.rect.width)


                elif randomPattern == 1 : #pattern polynome
                    ennemi.pattern = PatternPolynome(randint(-2,2)/1000,randint(-5,5)/1000,(randint(0,2)-1)*randint(100,300))
                    if ennemi.pattern.dir == -1 :
                        ennemi.posX=constantes.largeur
                    elif ennemi.pattern.dir == 1 :
                        ennemi.posX=0
                    #ennemi.pattern=PatternPolynome(-1/1000,1/200,150)


                elif randomPattern == 2 : #pattern cercle
                    ennemi.pattern = PatternCercle(randint(-200,constantes.largeur+200),randint(-100,constantes.hauteur-200),1,1,1)
                    ennemi.pattern = PatternCercle(randint(0,constantes.largeur),randint(0,constantes.hauteur-200),1,1,1)
                    rand= randint(1,3)
                    if rand== 1 :
                        ennemi.posY= -5-ennemi.rect.height
                        ennemi.posX= randint(-5,constantes.largeur)
                    else:
                        ennemi.posY= randint(-5,constantes.hauteur-100)
                        if rand==2:
                            ennemi.posX=-5-ennemi.rect.width
                        else :
                            ennemi.posX=constantes.largeur+5
                    ennemi.pattern.rayon=sqrt(pow(ennemi.posX-ennemi.pattern.centreX,2)+pow(ennemi.posY-ennemi.pattern.centreY,2))
                    #print(ennemi.posX,ennemi.posY,ennemi.pattern.centreX,ennemi.pattern.centreY,ennemi.pattern.rayon)
                    ennemi.pattern.vitesse=randint(3,10)/ennemi.pattern.rayon/6*pi
                    if ennemi.posX<ennemi.pattern.centreX and ennemi.posY>ennemi.pattern.centreY or ennemi.posX>ennemi.pattern.centreX and ennemi.posY<ennemi.pattern.centreY :   #je suis pas sûr pour cette condition encore mais elle semble bonne
                        ennemi.pattern.vitesse=-ennemi.pattern.vitesse  #en gros on inverse le sens dans les 2 cas où c'est nécessaire
                    ennemi.pattern.angle=abs(acos((ennemi.posX-ennemi.pattern.centreX)/ennemi.pattern.rayon))
                    if ennemi.posY-ennemi.pattern.centreY<0:
                        ennemi.pattern.angle=-ennemi.pattern.angle
                    #ennemi.pattern.angle=ennemi.pattern.angle*180/pi #conversion en degrés
                    #print(ennemi.pattern.deplacer(5,5))
                    #print(ennemi.pattern.centreX,ennemi.pattern.centreY,ennemi.pattern.angle,ennemi.pattern.vitesse,ennemi.pattern.rayon)
                    #print("-------")


                elif randomPattern == 3 : #zigzag
                    ennemi.pattern= PatternZigZag(randint(10,30),randint(1,5))
                    rand= randint(1,3)
                    if rand== 1 :
                        ennemi.posY= -5-ennemi.rect.height
                        ennemi.posX= randint(-5,constantes.largeur)
                        ennemi.pattern.mv_x = 0
                        ennemi.pattern.mv_y = 1
                    else:
                        ennemi.posY= randint(-5,constantes.hauteur-100)
                        ennemi.pattern.mv_y = 0
                        if rand==2:
                            ennemi.posX=-5-ennemi.rect.width
                            ennemi.pattern.mv_x = 1
                        else :
                            ennemi.posX=constantes.largeur+5
                            ennemi.pattern.mv_x = -1
                    ennemi.pattern.compteur = -150

                elif randomPattern == 4 :
                    ennemi.pattern = PatternSinusoidal(randint(10,50)*3,(randint(0,1)-0.5)*2,randint(10,constantes.hauteur-50)-150)
                    if ennemi.pattern.direction == -1 :
                        ennemi.posX=constantes.largeur+5




                #ennemi.posY = 5
                #ennemi.posX =  randint(0, constantes.largeur-ennemi.rect.width)
                ennemi.rect.x = ennemi.posX
                ennemi.rect.y = ennemi.posY
                #print("Apparition aux coordonnées :", ennemi.posX, ",", ennemi.posY)
                #print("Son rect est :", ennemi.rect)
                #print("--------------------------------------")
                """rand= randint(1,3)
                if rand== 1 :#en haut
                    ennemi.posY= -5
                    ennemi.posX= randint(-5,350)
                    print("En haut !")
                else:
                    ennemi.posY= randint(-5,350)#je pense pas que le jeu fasse la largeur de l'écran alors il faudra changer cette valeur quand on saura
                    if rand==2:
                        print("Heu... Sur la gauche ?")
                        ennemi.posX=-5
                    else :
                        ennemi.posX=350#idem ici
                        print("Sur la droite, je pense.")"""
                break
        return ennemi

    #TODO: Rajouter une fonction __repr__() pour qu'on puisse voir clairement un niveau, et l'éditer s'il le faut.


