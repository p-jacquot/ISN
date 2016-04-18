# Créé par PJACQUOT, le 21/03/2016 en Python 3.2
import pygame
from jeu import Jeu
from fenetre import Fenetre
from molecule import Molecule
from dialogue import Dialog
from niveau import Niveau
import constantes
from pattern import *
import pickle
pygame.init()
def testplay():
    jeu.moleculeJoueur = Molecule('oxygene.png', 30, 30,Pattern(0,0))
    jeu.moleculeJoueur.posX = 50
    jeu.moleculeJoueur.rect = jeu.moleculeJoueur.rect.move(50, 0)
    jeu.ennemyList.append(Molecule('azote.png', 35, 35,PatternCercle(50,60,10,4,3)))

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

pygame.init()
fenetre = Fenetre("test ISN Dialogue", 768, 600)
fenetre.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()

jeu = Jeu(fenetre, 1)
#testDialog()
#testSerializedDialogue()
testplay()
pygame.quit()
