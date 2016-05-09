# Créé par Pierre, le 07/05/2016 en Python 3.2

import pygame
import sys
import constantes

from menu import *
from fenetre import *
from jeu import *
from niveau import *


pygame.init()
pygame.mixer.init()

fenetre = Fenetre("Hydrogène II : Le retour", constantes.largeur, constantes.hauteur)

menu = Menu()
menu.init(['Nouvelle Partie', 'Continuer', 'Choix du Niveau', 'Options', 'Quitter'], fenetre.fen)
menu.draw()
pygame.key.set_repeat(199,69)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                menu.draw(-1)
            if event.key == K_DOWN:
                menu.draw(1)
            if event.key == K_RETURN:
                if menu.get_position() == 0:
                    jeu = Jeu(fenetre, Niveau(1), Molecule('hydrogene.png', Pattern(0,0)), 4.5)
                    jeu.progressInLevel()
                    sombre = pygame.Surface((constantes.largeur, constantes.hauteur))
                    sombre.set_alpha(255)
                    sombre.fill((0, 0, 0))
                    fenetre.fen.blit(sombre, (0,0))
                    pygame.display.flip()
                    menu.draw()
                    pygame.display.update()
                if menu.get_position() == 4:
                    pygame.display.quit()
                    sys.exit()
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            pygame.display.update()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.wait(8)