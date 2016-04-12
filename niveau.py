# Créé par Pierre, le 05/03/2016 en Python 3.2

import random
from dialogue import Dialog

class Niveau:
    """La classe qui gère les niveaux."""

    def __init__(self, mobOnScreen, totalMob):
        self.mobList = [] #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        self.maxMobOnScreen = mobOnScreen #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLeft = totalMob

    def __init__(self, numero, firstDialog, middleDialog, lastDialog):
        fname=str("resources/niveau/"+str(numero)+".txt")
        with open(fname) as text:
            content = text.readlines()
        self.mobList=[]    #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        for a in content[:-2]:
            print(a)
            print(a[-3:-1])
            self.mobList.append([str(a[:-4]),int(a[-3:-1])])
        print(self.mobList)
        self.maxMobOnScreen = content[-2] #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLeft = content[-1]
        self.firstDialog = firstDialog  #Les différents dialogues qu'ils y aura dans le niveau.
        self.middleDialog = middleDialog
        self.lastDialog = lastDialog


    def genererMob(self):
        rand = random.randint(0, 100)
        for mob in mobList:
            if rand < mob[1]:
                ennemi= mob[0] #On retourne la molécule.
                #code pour donner des coordonnees à l'ennemi, peut etre qu'on changera ca apres mais je pense que c'est nécessaire
                rand=random.randint(1,3)
                if rand== 1 :#en haut
                    ennemi.posY= -5
                    ennemi.posX=random.randint(-5,350)
                else:
                    ennemi.posY=random.randint(-5,350)#je pense pas que le jeu fasse la largeur de l'écran alors il faudra changer cette valeur quand on saura
                    if rand==2:
                        ennemi.posX=-5
                    else :
                        ennemi.posX=350#idem ici
                return ennemi

    #TODO: Rajouter une fonction __repr__() pour qu'on puisse voir clairement un niveau, et l'éditer s'il le faut.


