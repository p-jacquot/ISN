# Créé par PJACQUOT, le 21/03/2016 en Python 3.2
import pygame
from jeu import Jeu
from fenetre import Fenetre
from molecule import Molecule
from dialogue import Dialog
from niveau import Niveau

def testplay():
    jeu.moleculeJoueur = Molecule('resources/photos/oxygene.png', 30, 30)
    jeu.moleculeJoueur.posX = 50
    jeu.moleculeJoueur.rect = jeu.moleculeJoueur.rect.move(50, 0)
    jeu.ennemyList.append(Molecule('resources/photos/azote.png', 35, 35))

    jeu.play()

def testDialog():
    ricken = pygame.image.load("Ricken.png").convert_alpha()
    tharja = pygame.image.load("Tharja.png").convert_alpha()
    dialogue = Dialog(tharja, "Tharja", ricken, "Ricken")
    dialogue.punchlineList.append(["Il semblerait que mon sort n'ait pas fonctionné...", 0, dialogue.leftPosition])
    dialogue.punchlineList.append(["Hein ? Tu as dit quelque chose ?", 1, dialogue.rightPosition])
    jeu.dialoguer(dialogue)


fenetre = Fenetre("test", 768, 600)
fenetre.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()

jeu = Jeu(fenetre, 1)
testDialog()
pygame.quit()



