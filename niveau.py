# Créé par Pierre, le 05/03/2016 en Python 3.2

import random
from dialogue import Dialog

class Niveau:
    """La classe qui gère les niveaux."""

    def __init__(self, mobOnScreen, totalMob):
        self.mobList = [] #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        self.maxMobOnScreen = mobOnScreen #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLeft = totalMob

    def __init__(self, mobOnScreen, totalMob, firstDialog, middleDialog, lastDialog):
        self.mobList = [] #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        self.maxMobOnScreen = mobOnScreen #le nombre maximal de méchant qu'il pourrait y avoir en même temps.
        self.totalMobsLef = totalMob
        self.firstDialog = firstDialog  #Les différents dialogues qu'ils y aura dans le niveau.
        self.middleDialog = middleDialog
        self.lastDialog = lastDialog


    def genererMob(self):
        rand = random.randint(0, 100)
        for mob in mobList:
            if rand < mob[1]:
                return mob[0] #On retourne la molécule.

    #TODO: Rajouter une fonction __repr__() pour qu'on puisse voir clairement un niveau, et l'éditer s'il le faut.


