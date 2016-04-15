# Créé par Pierre, le 17/03/2016 en Python 3.2
import pygame

"""Constantes projectiles"""
pygame.init()
projectilesList = [ pygame.image.load("resources/photos/photon_bleu_clair_pour_le_joueur2.png").convert_alpha(),
                    pygame.image.load("resources/photos/photon_bleu.png").convert_alpha(),
                    pygame.image.load("resources/photos/photon_jaune.png").convert_alpha(),
                    pygame.image.load("resources/photos/photon_rose2.png").convert_alpha(),
                    pygame.image.load("resources/photos/photon_sombre.png").convert_alpha(),
                    pygame.image.load("resources/photos/photon_vert.png").convert_alpha(),
                    pygame.image.load("resources/photos/photon_violet.png").convert_alpha()]

#Quand vous voulez récupérer l'image d'un photon : projectilesList[index]