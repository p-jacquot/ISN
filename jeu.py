# Créé par Pierre, le 05/03/2016 en Python 3.2

from fenetre import Fenetre
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

        self.continuer = false
        self.moleculeJoueur = Atome()  #bon ok, c'est un atome...

    def play(self):
        while self.continuer:
            #La boucle principale du jeu.
            #print("yolo ! On s'amuse bien !")
            er = [] #surfaces ennemies
            epr = [] #surfaces des projectiles ennemis (et pas de l'éducation physique et sportive !)
            pjr = [] #surfaces des projectiles du joueur.
            for ennemy in self.ennemyList:
                ennemy.move()
                er.append(ennemy.rect)
            for proj in self.ennemyProjectiles:
                proj.move()
                epr.append(proj.rect)
            for proj in self.projectilesJoueur:
                proj.move()
                pjr.append(proj.rect)

            """Events incoming !"""
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                """Lorsqu'on appuie sur une touche. Ces valeurs ne sont là qu'a titre d'exemple, il faudra qu'on les modifies."""
                if event == K_UP:
                    self.moleculeJoueur.mv_y = -1
                elif event == K_DOWN:
                    self.moleculeJoueur.mv_y = 1
                elif event == K_LEFT:
                    self.moleculeJoueur.mv_x = -1
                elif event == K_RIGHT:
                    self.moleculeJoueur.mv_x = 1
            elif event.type == KEYUP:
                """Lorsqu'on relâche une touche."""
                if event == K_UP and self.moleculeJoueur.mv_y==-1:
                    self.moleculeJoueur.mv_y = 0
                elif event == K_DOWN and self.moleculeJoueur.mv_y==1:
                    self.moleculeJoueur.mv_y = 0
                elif event == K_LEFT and self.moleculeJoueur.mv_x==-1:
                    self.moleculeJoueur.mv_x = 0
                elif event == K_RIGHT and self.moleculeJoueur.mv_x==1:
                    self.moleculeJoueur.mv_x = 0
            #TODO: Gérer les collisions.


    def actualiser():
        self.fenetre.entites = self.ennemyList + self.ennemyProjectiles + self.projectilesJoueur + self.moleculeJoueur

    def stop(self):
        #si on veut faire des choses particulières une fois qu'on arrête le jeu.
        self.continuer = false

    def changeNiveau(self, niveau):
        """Cette fonction s'occupera de charger tout ce dont on a besoin d'un niveau :
            mobs, probas..."""
        self.niveau = niveau




