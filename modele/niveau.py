# Créé par Pierre, le 05/03/2016 en Python 3.2

import random

class Niveau:
    """La classe qui gère les niveaux."""

    def __init__(self):
        self.mobList = [[]] #Les choses sont stockées dans l'ordre suivant : molécule, proba d'apparition.
        self.maxMobOnScreen = 0 #le nombre maximal de méchant qu'il pourrait y avoir en même temps.


    def genererMob(self):
        rand = random.randint(0, 100)
        for mob in mobList:
            if rand < mob[1]:
                return mob[0] #On retourne la molécule.

    #TODO: Rajouter une fonction __repr__() pour qu'on puisse voir clairement un niveau, et l'éditer s'il le faut.


