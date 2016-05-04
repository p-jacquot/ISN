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
import niveau

pygame.init()

def testplay():

    jeu.moleculeJoueur = Molecule('hydrogene.png', Pattern(0,0))

    jeu.moleculeJoueur.posX = constantes.largeur/2
    jeu.moleculeJoueur.posY = constantes.hauteur-35
    jeu.moleculeJoueur.rect = jeu.moleculeJoueur.rect.move(jeu.moleculeJoueur.posX, jeu.moleculeJoueur.posY)
    jeu.moleculeJoueur.hp = 10
    jeu.vitesse = 0.4
    """jeu.ennemyList.append(Molecule('azote.png', PatternCercle(150,60,25,4,2)))
    jeu.ennemyList.append(Molecule('oxygene.png', PatternZigZag(20,1)))
    jeu.ennemyList.append(Molecule('carbone.png', PatternPolynome(1,1,1)))"""
    #jeu.ennemyList.append(Molecule('cortizone.png', Pattern(0,0)))

    """for a in jeu.ennemyList:
        a.posX =randint(15,200)
        a.posY = randint(15,200)"""
    #jeu.ennemyList.append(Molecule('hydrogene.png', PatternSinusoidal(5,1)))
    jeu.progressInLevel()

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
pygame.mixer.init()
fenetre = Fenetre("test ISN Dialogue", constantes.largeur, constantes.hauteur)
fenetre.fond = pygame.image.load("resources/galaxie.jpg").convert_alpha()

with open('resources/niveau/1/firstDialog.pickle', 'rb') as file:
    firstDialog = pickle.load(file)

with open('resources/niveau/1/middleDialog.pickle', 'rb') as file:
    middleDialog = pickle.load(file)

with open('resources/niveau/1/lastDialog.pickle', 'rb') as file:
    lastDialog = pickle.load(file)

jeu = Jeu(fenetre, Niveau(1,firstDialog, middleDialog, lastDialog))
for explode in constantes.explodeList:
    explode = explode.convert_alpha()
#testDialog()
#testSerializedDialogue()
testplay()
pygame.quit()
