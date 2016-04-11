# Créé par Pierre, le 06/04/2016 en Python 3.2
from math import *
from random import *
"""utiliser un tuple pour donner les arguments dans le constructeur est bcp plus simple pour créer le pattern"""
class Pattern:
    """La classe pattern dont tous les pattern doivent hériter."""
    def __init__(self, data):
        self.mv_x = data[0]
        self.mv_y = data[1]

    def deplacer(self, posX, posY):
        """La fonction deplace doit retourner x et y."""
        posX += self.mv_x
        posY += self.mv_y
        return posX, posY

class PatternPolynome(Pattern):
    """Pattern qui fait se déplacer selon un polynome du second degré."""
    def __init__(self, a, b, c):
        self.a = data[0]
        self.b = data[1]
        self.c = abs(data[2])  #je pense pas qu'on aura une ordonnée à l'origine en dehors de l'écran
        if data[2] == sqrt(pow(x,2)):# le signe de c donne la direction de x
            self.dir = 1
        else:
            self.dir = -1

    def deplacer(self, posX, posY):
        posX += self.dir
        posY = self.a * posX * posX + self.b * posX - self.c
        return posX, posY

class PatternCercle(Pattern):
    """Pattern qui fait se déplacer selon un cercle au milieu de l'écran"""
    def __init__(self,data):
        self.centreX=data[0]
        self.centreY=data[1]
        self.rayon=data[2]
        self.angle=data[3]
        self.vitesse=data[4] #en degrés par mouvement et négatif pour tourner dans l'autre sens

    def deplacer(self,posX,posY):
        self.angle+=vitesse
        posX=centreX+rayon*(cos(angle/180*pi))
        posY=centreY+rayon*(sin(angle/180*pi))
        return posX,posY

class PatternZigZag(Pattern):#je ne suis pas sûr de la syntaxe pour ce pattern
    def __init__(self,data):
        self.tempsMax=abs(data[0])#temps entre les changements de direction(en nb defois où on appelle move)
        self.compteur=9001
        self.vitesse=abs(data[1])

    def deplacer(self,posX,posY):
        compteur+=1
        if self.compteur>self.temps:
            #self.Pattern.__del__()
            #self.Pattern=Pattern(randint(-vitesse,vitesse),randint(-vitesse,vitesse))
            mv_x=randint(-vitesse,vitesse)
            mv_y=randint(-vitesse,vitesse)
            self.compteur=-2
        posX+=mv_x
        posY+=mv_y
        return posX,posY
        #return self.Pattern.deplacer(posX,posY)

class PatternSinusoidal(Pattern):
    def __init__(self,data):
        self.amplitude=data[0]
        self.direction=data[1]

    def deplacer(self,posX,posY):
        posX+=self.direction
        posY = self.amplitude *sin(posX/180*pi)
        return posX,posY

