# Créé par PJACQUOT, le 21/03/2016 en Python 3.2
import pygame
from jeu import Jeu
from fenetre import Fenetre
from molecule import Molecule
from dialogue import Dialog
from niveau import Niveau

import pickle

def testplay():
    jeu.moleculeJoueur = Molecule('resources/photos/oxygene.png', 30, 30)
    jeu.moleculeJoueur.posX = 50
    jeu.moleculeJoueur.rect = jeu.moleculeJoueur.rect.move(50, 0)
    jeu.ennemyList.append(Molecule('resources/photos/azote.png', 35, 35))

    jeu.play()

def testDialog():
    #ricken = pygame.image.load("resources/temporaire/Ricken.png").convert_alpha()
    #tharja = pygame.image.load("resources/temporaire/Tharja.png").convert_alpha()
    dialogue = Dialog("resources/temporaire/Tharja.png", "Tharja", (10, 210), "resources/temporaire/Ricken.png", "Ricken", (500, 200))
    dialogue.punchlineList.append(["Il semblerait que mon sort n'ait pas fonctionné...", 0])
    dialogue.punchlineList.append(["Hein ? Tu as dit quelque chose ?", 1])
    dialogue.punchlineList.append(["Non non... Rien... hé hé...", 0])
    with open('dialogue.pickle', 'wb') as file:
        pickle.dump(dialogue, file)
    jeu.dialoguer(dialogue)

def testSerializedDialogue():
    with open('resources/temporaire/dialogue.pickle', 'rb') as file:
        dialogue = pickle.load(file)
    jeu.dialoguer(dialogue)

fenetre = Fenetre("test ISN Dialogue", 768, 600)
fenetre.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()

jeu = Jeu(fenetre, 1)
#testDialog()
testSerializedDialogue()
pygame.quit()
