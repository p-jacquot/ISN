# Créé par Pierre, le 06/04/2016 en Python 3.2
from math import *
from random import *
"""utiliser un tuple pour donner les arguments dans le constructeur est bcp plus simple pour créer le pattern"""
class Pattern:
    """La classe pattern dont tous les pattern doivent hériter."""
    def __init__(self, mv_x,mv_y):
        self.mv_x = mv_x
        self.mv_y = mv_y

    def deplacer(self, posX, posY):
        """La fonction deplace doit retourner x et y."""
        posX += self.mv_x
        posY += self.mv_y
        return posX, posY

class PatternPolynome(Pattern):
    """Pattern qui fait se déplacer selon un polynome du second degré."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = abs(c)  #je pense pas qu'on aura une ordonnée à l'origine en dehors de l'écran
        if c == abs(c):# le signe de c donne la direction de x
            self.dir = 1
        else:
            self.dir = -1

    def deplacer(self, posX, posY):
        posX += self.dir
        posY = self.a * posX * posX + self.b * posX - self.c
        return posX, posY

class PatternCercle(Pattern):
    """Pattern qui fait se déplacer selon un cercle au milieu de l'écran"""
    def __init__(self,centreX,centreY,rayon,angle,vitesse):
        self.centreX=centreX
        self.centreY=centreY
        self.rayon=rayon
        self.angle=angle
        self.vitesse=vitesse #en degrés par mouvement et négatif pour tourner dans l'autre sens

    def deplacer(self,posX,posY):
        self.angle+=self.vitesse
        posX=self.centreX+self.rayon*(cos(self.angle/180*pi))
        posY=self.centreY+self.rayon*(sin(self.angle/180*pi))
        return posX,posY

class PatternZigZag(Pattern):#je ne suis pas sûr de la syntaxe pour ce pattern
    def __init__(self,tempsMax,vitesse):
        self.tempsMax=abs(tempsMax)#temps entre les changements de direction(en nb defois où on appelle move)
        self.compteur=9001
        self.vitesse=abs(vitesse)
        self.temps=tempsMax

    def deplacer(self,posX,posY):
        self.compteur+=1
        if self.compteur>self.temps:
            #self.Pattern.__del__()
            #self.Pattern=Pattern(randint(-vitesse,vitesse),randint(-vitesse,vitesse))
            self.mv_x=randint(-self.vitesse,self.vitesse)
            self.mv_y=randint(-self.vitesse,self.vitesse)
            self.compteur=-2
        posX+=self.mv_x
        posY+=self.mv_y
        return posX,posY
        #return self.Pattern.deplacer(posX,posY)

class PatternSinusoidal(Pattern):
    def __init__(self,amplitude,direction):
        self.amplitude=amplitude
        self.direction=direction

    def deplacer(self,posX,posY):
        posX+=self.direction
        posY = self.amplitude *sin(posX/180*pi)
        return posX,posY

