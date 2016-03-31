# Créé par Pierre, le 05/03/2016 en Python 3.2

from fenetre import Fenetre
import pygame
from pygame.event import *
from pygame.locals import * #Pour les events.

class Jeu:
    """La classe qui s'occupera de gérer le jeu en lui même"""

    def __init__(self, fenetre, niveau): #on lui donnera le niveau qu'on veut jouer (un int, et on ira chercher dans des dossiers).
        self.fenetre = fenetre
        self.changeNiveau(niveau)

        self.ennemyList = [] #les molécules méchantes
        self.ennemyProjectiles = [] #les projectiles des molécules méchantes
        self.projectilesJoueur = [] #les projectiles de la molécule gentille.

        self.continuer = True
        self.moleculeJoueur = None
        #self.moleculeJoueur = Atome()  #bon ok, c'est un atome...

    def play(self):
        er = [] #rect ennemies
        epr = [] #rect des projectiles ennemis
        pjr = [] #rect des projectiles du joueur.
        while self.continuer:
            #La boucle principale du jeu.
            #print("yolo ! On s'amuse bien !")
            #print(self.moleculeJoueur.rect)
            """Mouvement des différentes molecules et projectiles"""
            for ennemy in self.ennemyList:
                ennemy.move()
                er.append(ennemy.rect)
                print(ennemy.rect)
            for proj in self.ennemyProjectiles:
                proj.move()
                epr.append(proj.rect)
            for proj in self.projectilesJoueur:
                proj.move()
                pjr.append(proj.rect)

            """Calcul des collisions."""
            indexMechant = self.moleculeJoueur.rect.collidelist(er)
            if indexMechant != -1:
                self.moleculeJoueur.hp -= 1
                self.ennemyList[indexMechant].hp -= 1

            indexMechantProjectile = self.moleculeJoueur.rect.collidelist(epr)
            if indexMechantProjectile != -1:
                self.moleculeJoueur.hp -= 1
                del self.ennemyProjectiles[indexMechantProjectile] #On supprime le projectile, s'il a touché sa cible.

            for proj in pjr:
                index = proj.collidelist(er)
                if index != -1:
                    self.ennemyList[index].hp -= 1

            """Events incoming !"""
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                print("Touche appuyée.")
                """Lorsqu'on appuie sur une touche. Ces valeurs ne sont là qu'a titre d'exemple, il faudra qu'on les modifies."""
                if event.key == K_UP:
                    self.moleculeJoueur.mv_y = -1
                elif event.key == K_DOWN:
                    print("C'est la touche bas.")
                    self.moleculeJoueur.mv_y = 1
                elif event.key == K_LEFT:
                    self.moleculeJoueur.mv_x = -1
                elif event.key == K_RIGHT:
                    self.moleculeJoueur.mv_x = 1
            elif event.type == KEYUP:
                """Lorsqu'on relâche une touche."""
                if event.key == K_UP and self.moleculeJoueur.mv_y==-1:
                    self.moleculeJoueur.mv_y = 0
                elif event.key == K_DOWN and self.moleculeJoueur.mv_y==1:
                    self.moleculeJoueur.mv_y = 0
                elif event.key == K_LEFT and self.moleculeJoueur.mv_x==-1:
                    self.moleculeJoueur.mv_x = 0
                elif event.key == K_RIGHT and self.moleculeJoueur.mv_x==1:
                    self.moleculeJoueur.mv_x = 0
            elif event.type == QUIT:
                self.fenetre.fermer()
                self.continuer = False
            self.moleculeJoueur.move()
            self.actualiser()
            #TODO: Gérer les collisions.
        self.fenetre.fermer()

    def actualiser(self):
        self.fenetre.entites.extend(self.ennemyList)
        self.fenetre.entites.extend(self.ennemyProjectiles)
        self.fenetre.entites.extend(self.projectilesJoueur)
        self.fenetre.entites.append(self.moleculeJoueur)
        self.fenetre.rafraichir()

    def dialoguer(self, dialog):
        while dialog.isNotFinished:
            punchline = dialog.getPunchline()
            posX, posY = punchline[2]
            self.fenetre.fen.blit(punchline[1][1], (posX, posY))
            self.fenetre.dessinerCadre(posX, posY, self.fenetre.largeur, 100)
            self.fenetre.dessinerCadre(posX+50, posY-25, 75, 30)
            self.fenetre.ecrireText(punchline[1][0], posX + 55, posY - 20)
            self.fenetre.ecrireText(punchline[0], posX, posY +20)
            event = pygame.event.wait()
            while event.type != KEYDOWN:
                pass

    def stop(self):
        #si on veut faire des choses particulières une fois qu'on arrête le jeu.
        self.continuer = false

    def changeNiveau(self, niveau):
        """Cette fonction s'occupera de charger tout ce dont on a besoin d'un niveau :
            mobs, probas..."""
        self.niveau = niveau




