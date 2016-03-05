# Créé par Pierre, le 03/03/2016 en Python 3.2

class Projectile:
    """Classe des projectiles tirés par les atomes."""

    def __init__(self, pos, mv):
        """Constructeur 'tout simple'..."""
        self.position = pos #tuple de position.
        self.mouvement = mv #tuple de mouvement.

    def __init__(self, pos, posCible):
        """Le fameux constructeur qui va permettre de viser le joueur."""
        self.position = pos
        x1, y1 = pos
        x2, y2 = posCible
        a = int((y2-y1)/(x2-x1))
        b = y1 - a*x1
        self.mouvement = (a,b)

    def move(self):
        self.position += self.mouvement

