# Créé par Pierre, le 06/04/2016 en Python 3.2
from math import *
class Pattern:
    """La classe pattern dont tous les pattern doivent hériter."""
    def __init__(self, mv_x, mv_y):
        self.mv_x = mv_x
        self.mv_y = mv_y

    def deplacer(self, posX, posY):
        """La fonction deplace doit retourner x et y."""
        posX += self.mv_x
        posY += self.mv_y
        return posX, posY

class PatternDroit(Pattern):
    """Pattern qui fait se déplacer selon un polynome du second degré."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if c == sqrt(pow(x,2)):
            self.dir = 1
        else:
            self.dir = -1

    def deplacer(self, posX, posY):
        posX += self.dir
        posY = self.a * self.a * posX + self.b * posX + self.c
        return posX, posY