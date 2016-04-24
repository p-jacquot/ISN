# Créé par Pierre, le 17/03/2016 en Python 3.2
import pygame
pygame.init()
"""Constantes projectiles"""
projectilesList = [ pygame.image.load("resources/photos/photon_bleu_clair_pour_le_joueur2.png"),
                    pygame.image.load("resources/photos/photon_bleu.png"),
                    pygame.image.load("resources/photos/photon_jaune.png"),
                    pygame.image.load("resources/photos/photon_rose2.png"),
                    pygame.image.load("resources/photos/photon_sombre.png"),
                    pygame.image.load("resources/photos/photon_vert.png"),
                    pygame.image.load("resources/photos/photon_violet.png")]

"""Les sprites des explosions"""
explodeList = [pygame.image.load("resources/photos/explosion_v1.1.bmp"),
               pygame.image.load("resources/photos/explosion_v2.2.bmp"),
               pygame.image.load("resources/photos/explosion_v3.bmp")]
#Quand vous voulez récupérer l'image d'un photon : projectilesList[index]

#lycee
largeur,hauteur= 768, 600

#pas lycee
#largeur,hauteur=1280,720