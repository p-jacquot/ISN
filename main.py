# Créé par Pierre, le 07/05/2016 en Python 3.2

import pygame
import sys
import constantes
import pickle
from menu import *
from fenetre import *
from jeu import *
from niveau import *


pygame.init()
pygame.mixer.init()

with open("options.pickle", 'rb') as file:
        donnees = pickle.load(file)
constantes.niveauActuel = donnees[0]
constantes.niveauMaxAtteint = donnees[1]
constantes.hauteur=donnees[2]
constantes.largeur=donnees[3]


fenetre = Fenetre("Hydrogène II : Le retour", constantes.largeur, constantes.hauteur)

menu = Menu()
menu.init(['Nouvelle Partie', 'Continuer', 'Choix du Niveau', 'Replay', 'Options', 'Quitter'], fenetre.fen)
menu.draw()
pygame.key.set_repeat(199,69)
pygame.display.update()
"""def choixNiveau() :

        choix = Menu()
        listeNiveaux = []
        for a in range(constantes.niveauMaxAtteint):
            listeNiveaux.append(str(a+1))
        choix.init(listeNiveaux, fenetre.fen)
        choix.draw()
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
                        jeu = Jeu(fenetre, Niveau(menu.get_position()+1), Molecule('hydrogene.png', Pattern(0,0)), 4.5)
                        constantes.niveauActuel = menu.get_position()+1
                        jeu.progressInLevel()
                        sombre = pygame.Surface((constantes.largeur, constantes.hauteur))
                        sombre.set_alpha(255)
                        sombre.fill((0, 0, 0))
                        fenetre.fen.blit(sombre, (0,0))
                        pygame.display.flip()
                        menu.draw()
                        pygame.display.update()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    pygame.display.update()
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.wait(8)"""#code tout pourri qu'il faut pas prendre en compte mais je le garde pour l'instant pour récupérer les fonctions quand j'en aurai besoin
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
                    constantes.niveauActuel = 1
                    constantes.sauvegarder()
                    jeu.progressInLevel()
                    sombre = pygame.Surface((constantes.largeur, constantes.hauteur))
                    sombre.set_alpha(255)
                    sombre.fill((0, 0, 0))
                    fenetre.fen.blit(sombre, (0,0))
                    pygame.display.flip()
                    menu.draw()
                    pygame.display.update()
                if menu.get_position() == 1:
                    jeu = Jeu(fenetre, Niveau(constantes.niveauActuel), Molecule('hydrogene.png', Pattern(0,0)), 4.5)
                    jeu.progressInLevel()
                    sombre = pygame.Surface((constantes.largeur, constantes.hauteur))
                    sombre.set_alpha(255)
                    sombre.fill((0, 0, 0))
                    fenetre.fen.blit(sombre, (0,0))
                    pygame.display.flip()
                    menu.draw()
                    pygame.display.update()
                if menu.get_position() == 2 :
                    #choixNiveau()
                    pass
                if menu.get_position() == len(menu.liste)-1:
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

