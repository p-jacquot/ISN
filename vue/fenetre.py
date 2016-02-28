# Créé par Pierre, le 28/02/2016 en Python 3.2

import pygame

def __init__(self, titre, largeur, hauteur):
    pygame.init()
    self.fenetre = pygame.display.set_mode((largeur, hauteur))
    fond = pygame.image.load("hakase_nyan.png").convert()
    self.fenetre.blit(fond, (0, 0))

