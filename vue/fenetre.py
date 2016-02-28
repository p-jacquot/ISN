# Créé par Pierre, le 28/02/2016 en Python 3.2

import pygame

class Fenetre:
    """Classe Fenêtre, s'occupant de l'affichage."""

    def __init__(self, titre, largeur, hauteur):
        pygame.init()
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption(titre)
        fond = pygame.image.load("hakase_nyan.png").convert_alpha()
        self.fenetre.blit(fond, (0, 0))
        #TODO : ajouter un titre à la fenêtre.

    def __del__(self):
        """Possible qu'on n'ait pas à se servir de cette fonction, mais je l'ai créée quand même au cas où."""
        pygame.quit()

    def rafraichir(self):
        pygame.display.flip()

    def fermer(self):
        pygame.quit()