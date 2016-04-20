# Créé par Pierre, le 05/03/2016 en Python 3.2
from random import *
from fenetre import Fenetre
import pygame
from pygame.event import *
from pygame.locals import * #Pour les events.
pygame.init()
from projectiles import *
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
        self.delayTirJoueur=0
        self.tir = False
        #self.moleculeJoueur = Atome()  #bon ok, c'est un atome...

    def play(self):
        while self.continuer:
            er = [] #rect ennemies
            epr = [] #rect des projectiles ennemis
            pjr = [] #rect des projectiles du joueur.
            if len(self.ennemyList) > self.niveau.maxMobOnScreen :
                if randint(0,50)==45:
                    self.ennemyList.append(self.niveau.genererMob())
            #La boucle principale du jeu.
            #print("yolo ! On s'amuse bien !")
            #print(self.moleculeJoueur.rect)
            """Mouvement des différentes molecules et projectiles"""

            newList=[]
            for ennemy in self.ennemyList:
                if ennemy.dead==False:
                    ennemy.move()
                    er.append(ennemy.rect)
                    self.ennemyProjectiles+=ennemy.tirer()
                    newList.append(ennemy)
                elif ennemy.hp<=0:#l'ennemi n'a plus d'hp
                    ennemy.__del__()
                    #On met ici l'animation de mort, c'est à dire l'explosion, peut etre un score plus tard
                else:#l'ennemi sort de l'écran
                    ennemy.__del__()
                #print(ennemy.rect)
            self.ennemyList=newList

            newList=[]
            for proj in self.ennemyProjectiles:
                if proj.dead==False:
                   proj.move()
                   epr.append(proj.rect)
                   newList.append(proj)
                else:
                    proj.__del__()
            self.ennemyProjectiles=newList

            newList=[]
            for proj in self.projectilesJoueur:
                if proj.dead==False:
                    proj.move()
                    pjr.append(proj.rect)
                    newList.append(proj)
                else:
                    proj.__del__()
            self.projectilesJoueur=newList

            """Calcul des collisions."""
            indexMechant = self.moleculeJoueur.rect.collidelist(er)
            if indexMechant != -1:
                self.moleculeJoueur.hp -= 1
                self.ennemyList[indexMechant].hit()

            indexMechantProjectile = self.moleculeJoueur.rect.collidelist(epr)
            if indexMechantProjectile != -1:
                self.moleculeJoueur.hp -= 1
                self.ennemyProjectiles[indexMechantProjectile].dead=True #On supprime le projectile, s'il a touché sa cible.

            for proj in pjr:
                index = proj.collidelist(er)
                if index != -1:
                    self.ennemyList[index].hit()
                    self.projectilesJoueur[index].dead=True

            """Events incoming !"""
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                #print("Touche appuyée.")
                """Lorsqu'on appuie sur une touche. Ces valeurs ne sont là qu'a titre d'exemple, il faudra qu'on les modifies."""
                if event.key == K_UP:
                    self.moleculeJoueur.pattern.mv_y = -1
                elif event.key == K_DOWN:
                    #print("C'est la touche bas.")
                    self.moleculeJoueur.pattern.mv_y = 1
                elif event.key == K_LEFT:
                    self.moleculeJoueur.pattern.mv_x = -1
                elif event.key == K_RIGHT:
                    self.moleculeJoueur.pattern.mv_x = 1
                if event.key == K_SPACE :
                    self.tir =True
            elif event.type == KEYUP:
                """Lorsqu'on relâche une touche."""
                if event.key == K_UP and self.moleculeJoueur.pattern.mv_y==-1:
                    self.moleculeJoueur.pattern.mv_y = 0
                elif event.key == K_DOWN and self.moleculeJoueur.pattern.mv_y==1:
                    self.moleculeJoueur.pattern.mv_y = 0
                elif event.key == K_LEFT and self.moleculeJoueur.pattern.mv_x==-1:
                    self.moleculeJoueur.pattern.mv_x = 0
                elif event.key == K_RIGHT and self.moleculeJoueur.pattern.mv_x==1:
                    self.moleculeJoueur.pattern.mv_x = 0
                if event.key == K_SPACE :
                    self.tir = False
            elif event.type == QUIT:
                self.fenetre.fermer()
                self.continuer = False

            self.delayTirJoueur-=1
            if self.tir == True and self.delayTirJoueur <=0 :
                proj = Projectile(self.moleculeJoueur.posX,self.moleculeJoueur.posY,0,-3)
                proj.img = constantes.projectilesList[0].convert_alpha()
                self.projectilesJoueur.append(proj)
                self.delayTirJoueur=20

            self.moleculeJoueur.move()
            if self.moleculeJoueur.posX<10:
                self.moleculeJoueur.posX=10
            elif self.moleculeJoueur.posX>340:  #changer encore ici
                self.moleculeJoueur.posX=340
            if self.moleculeJoueur.posY <10:
                self.moleculeJoueur.posY=10
            elif self.moleculeJoueur.posY>590:
                self.moleculeJoueur.posY=590
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
        sombre = pygame.Surface((self.fenetre.largeur, self.fenetre.hauteur))  # the size of your rect
        sombre.set_alpha(128)
        sombre.fill((0, 0, 0))
        perso = []
        for liste in dialog.characters:
            img = pygame.image.load(liste[1]).convert_alpha()
            perso.append([liste[0], img, liste[2]])

        while dialog.notFinished:
            punchline = dialog.getPunchline()
            posX, posY = perso[punchline[1]][2]
            #print(punchline[1][0])
            #pygame.draw.rect(self.fenetre.fen, pygame.Color(0, 0, 0, 0), pygame.Rect(0, 0, self.fenetre.largeur, self.fenetre.hauteur))
            self.fenetre.fen.blit(sombre, (0,0))
            self.fenetre.fen.blit(perso[punchline[1]][1], (posX, posY))
            self.fenetre.dessinerCadre(0, 500, 100, self.fenetre.largeur)
            self.fenetre.dessinerCadre(posX+50, posY-25, 30, 100)
            self.fenetre.ecrireTexte(perso[punchline[1]][0], posX + 55, posY - 20)
            self.fenetre.ecrireTexte(punchline[0], 25, 500)
            event = pygame.event.wait()
            while event.type != KEYDOWN:
                event = pygame.event.wait()
                pass

    def progressInLevel(self):
        pygame.mixer.music.load(self.niveau.pathMusicBoss)
        pygame.mixer.music.play()

    def stop(self):
        #si on veut faire des choses particulières une fois qu'on arrête le jeu.
        self.continuer = false

    def changeNiveau(self, niveau):
        """Cette fonction s'occupera de charger tout ce dont on a besoin d'un niveau :
            mobs, probas..."""
        self.niveau = niveau




