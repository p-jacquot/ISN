# Créé par PJACQUOT, le 21/03/2016 en Python 3.2
import pygame
from jeu import Jeu
from fenetre import Fenetre
from molecule import Molecule

fenetre = Fenetre("test", 768, 600)
fenetre.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()

jeu = Jeu(fenetre, 1)

jeu.moleculeJoueur = Molecule('resources/photos/oxygene.png', 30, 30)
jeu.moleculeJoueur.posX = 50
jeu.moleculeJoueur.rect = jeu.moleculeJoueur.rect.move(50, 0)
jeu.ennemyList.append(Molecule('resources/photos/azote.png', 35, 35))

jeu.play()

