# Créé par Pierre, le 03/03/2016 en Python 3.2

class Projectile:
    """Classe des projectiles tirés par les atomes."""

    def __init__(self, pos, mv):
        self.position = pos #tuple de position.
        self.mouvement = mv #tuple de mouvement.

    def move(self):
        self.position += self.mouvement

