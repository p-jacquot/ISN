# Créé par Pierre, le 05/03/2016 en Python 3.2
from random import *
from fenetre import *
import pygame
from pygame.event import *
from pygame.locals import * #Pour les events.
pygame.init()
from projectiles import *
from pattern import *
from constantes import *
from replay import *
from niveau import *
pygame.mixer.init(frequency=22050, size=-16, channels=25, buffer=4096)
explosion1 = pygame.mixer.Sound("resources/explosion1.wav")
explosion2 = pygame.mixer.Sound("resources/explosion2.wav")
explosion1.set_volume(.5)
explosion2.set_volume(.5)
audioDialogue=pygame.mixer.Channel(0)

class Jeu:
    """La classe qui s'occupera de gérer le jeu en lui même"""

    def __init__(self, fenetre, niveau, moleculeJoueur, vitesse): #on lui donnera le niveau qu'on veut jouer (un int, et on ira chercher dans des dossiers).
        self.fenetre = fenetre
        self.niveau = niveau
        self.fenetre.setFond(self.niveau.fond)
        self.ennemyList = [] #les molécules méchantes
        self.ennemyProjectiles = [] #les projectiles des molécules méchantes
        self.projectilesJoueur = [] #les projectiles de la molécule gentille.

        self.continuer = True
        self.moleculeJoueur = moleculeJoueur
        self.delayTirJoueur = 0
        self.tir = False
        self.delayMouvement = 0
        self.typeProjJoueur =[  [(0,0,0,-3)],
                                [(-12,0,0,-3),(12,0,0,-3)],
                                [(-12,5,-0.5,-2.5),(0,0,0,-3),(12,5,0.5,-2.5)],
                                [(-15,5,-0.5,-2.5),(-8,0,0,-3),(8,0,0,-3),(15,5,0.5,-2.5)]]

        self.listeFrame=[]
        self.vitesse = vitesse
        self.moleculeJoueur.posX = constantes.largeur/2
        self.moleculeJoueur.posY = constantes.hauteur-35

        #self.moleculeJoueur = Atome()  #bon ok, c'est un atome...

    def play(self):
        pygame.time.Clock().tick(15)
        self.continuer = True
        self.clearProj()
        self.tir = False
        while self.continuer:
            er = [] #rect ennemies
            epr = [] #rect des projectiles ennemis
            pjr = [] #rect des projectiles du joueur.
            if len(self.ennemyList) < self.niveau.maxMobOnScreen and self.niveau.totalMobsLeft > 0:
                if randint(0,100)==45:
                    #print("On génère une nouvelle molécule !")
                    self.ennemyList.append(self.niveau.genererMob())
            #La boucle principale du jeu.
            #print("yolo ! On s'amuse bien !")
            #print(self.moleculeJoueur.rect)
            """Mouvement des différentes molecules et projectiles"""
            """if self.delayMouvement < 0 :
                self.delayMouvement = 10
            self.delayMouvement -= 1"""
            newList=[]
            #print(len(self.ennemyList))
            for ennemy in self.ennemyList:
                if ennemy.dead==False:
                    if self.delayMouvement == 0 :
                        ennemy.move()
                    er.append(ennemy.rect)
                    #er.append(ennemy.rect)
                    self.ennemyProjectiles+=ennemy.tirer()
                    newList.append(ennemy)
                elif ennemy.hp<=0:#l'ennemi n'a plus d'hp
                    ennemy.__del__()
                    explosion2.play()
                    #On met ici l'animation de mort, c'est à dire l'explosion, peut etre un score plus tard
                else:#l'ennemi sort de l'écran
                    ennemy.__del__()
                if ennemy.dying:
                    self.fenetre.explosions.append(ennemy.explodeCoords)
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
                explosion1.play()
                self.ennemyList[indexMechant].hit()
                self.clearProj()

            indexMechantProjectile = self.moleculeJoueur.rect.collidelist(epr)
            if indexMechantProjectile != -1:
                self.moleculeJoueur.hp -= 1
                explosion1.play()
                self.ennemyProjectiles[indexMechantProjectile].dead=True #On supprime le projectile, s'il a touché sa cible.
                #self.clearProj()

            for proj in self.projectilesJoueur:
                index = proj.rect.collidelist(er)
                if index != -1:
                    self.ennemyList[index].hit()
                    proj.dead=True

            """Events incoming !"""
            event = pygame.event.poll()
            if event.type == NOEVENT:
                #print('Pas d\'event !')
                pass
            elif event.type == KEYDOWN:
                #print("Touche appuyée.")
                """Lorsqu'on appuie sur une touche. Ces valeurs ne sont là qu'a titre d'exemple, il faudra qu'on les modifies."""
                if event.key == K_UP:
                    self.moleculeJoueur.pattern.mv_y = -1 * self.vitesse
                elif event.key == K_DOWN:
                    #print("C'est la touche bas.")
                    self.moleculeJoueur.pattern.mv_y = 1 * self.vitesse
                elif event.key == K_LEFT:
                    self.moleculeJoueur.pattern.mv_x = -1 * self.vitesse
                elif event.key == K_RIGHT:
                    self.moleculeJoueur.pattern.mv_x = 1 * self.vitesse
                if event.key == K_z :
                    self.tir =True
                if event.key == K_LSHIFT :
                    self.vitesse = 2
            elif event.type == KEYUP:
                """Lorsqu'on relâche une touche."""
                #print("Touche relachée !")
                if event.key == K_UP and self.moleculeJoueur.pattern.mv_y<0:
                    self.moleculeJoueur.pattern.mv_y = 0
                elif event.key == K_DOWN and self.moleculeJoueur.pattern.mv_y>0:
                    self.moleculeJoueur.pattern.mv_y = 0
                elif event.key == K_LEFT and self.moleculeJoueur.pattern.mv_x<0:
                    self.moleculeJoueur.pattern.mv_x = 0
                elif event.key == K_RIGHT and self.moleculeJoueur.pattern.mv_x>0:
                    self.moleculeJoueur.pattern.mv_x = 0
                if event.key == K_z:
                    self.tir = False
                if event.key == K_LSHIFT :
                    self.vitesse = 4.5
                if event.key == K_ESCAPE:
                    self.pause()
                """if event.key == K_r:
                    replay = Replay((constantes.largeur,constantes.hauteur),self.listeFrame)
                    nom = replay.nom
                    replay.saveReplay()
                    self.fenetre.playReplay(nom)"""
            elif event.type == QUIT:
                self.fenetre.fermer()
                self.continuer = False

            self.delayTirJoueur-=1
            if self.tir == True and self.delayTirJoueur <=0 :
                self.shootJoueur()

            if self.moleculeJoueur.dead or self.niveau.totalMobsLeft <= 0 and len(self.ennemyList) <= 0:
                self.continuer = False
                print("lel on quitte !")
            self.moleculeJoueur.move()
            if self.moleculeJoueur.posX<10:
                self.moleculeJoueur.posX=10
            elif self.moleculeJoueur.posX>constantes.largeur-40:  #changer encore ici
                self.moleculeJoueur.posX=constantes.largeur-40
            if self.moleculeJoueur.posY <10:
                self.moleculeJoueur.posY=10
            elif self.moleculeJoueur.posY>constantes.hauteur-40:
                self.moleculeJoueur.posY=constantes.hauteur-40
            self.actualiser()
            if constantes.recordOn :
                self.listeFrame.append(pygame.image.tostring(self.fenetre.fen,"RGB"))
                if len(self.listeFrame)>500 :
                    self.listeFrame = self.listeFrame[-500:]


    def actualiser(self):
        self.fenetre.entites.extend(self.ennemyList)
        self.fenetre.entites.extend(self.ennemyProjectiles)
        self.fenetre.entites.extend(self.projectilesJoueur)
        self.fenetre.entites.append(self.moleculeJoueur)
        self.fenetre.rafraichir()

    def dialoguer(self, dialog):
        """sombre = pygame.Surface((self.fenetre.largeur, self.fenetre.hauteur))
        sombre.set_alpha(128)
        sombre.fill((0, 0, 0))"""
        perso = []
        for liste in dialog.characters:
            img = pygame.image.load(liste[1]).convert_alpha()
            perso.append([liste[0], img, liste[2]])
        for p in perso:
            #print(p)
            #print(p[1].get_rect())
            rect = p[1].get_rect()
            rect.x, rect.y = p[2]
            p[2] = (rect.x, self.fenetre.hauteur - 100 - rect.height)
        while dialog.notFinished:
            punchline = dialog.getPunchline()
            posX, posY = perso[punchline[1]][2]
            #print(punchline[1][0])
            #pygame.draw.rect(self.fenetre.fen, pygame.Color(0, 0, 0, 0), pygame.Rect(0, 0, self.fenetre.largeur, self.fenetre.hauteur))
            self.fenetre.rafraichir()
            #self.fenetre.fen.blit(sombre, (0,0))
            self.fenetre.assombrir()
            self.fenetre.fen.blit(perso[punchline[1]][1], (posX, posY))
            self.fenetre.dessinerCadre(0, self.fenetre.hauteur-100, 100, self.fenetre.largeur)
            self.fenetre.dessinerCadre(posX+50, posY-25, 30, 100)
            self.fenetre.ecrireTexte(perso[punchline[1]][0], posX + 55, posY - 20)
            self.fenetre.ecrireTexte(punchline[0], 25, self.fenetre.hauteur-80)
            event = pygame.event.wait()
            #audio = pygame.mixer.Sound("resources/temporaire/"+str(dialog.counter)+".wav")
            #audioDialogue(audio)
            reading = True
            while reading:
                event = pygame.event.wait()
                if event.type == KEYDOWN:
                    if event.key == K_z:
                        reading = False


    def progressInLevel(self):
        play = True
        while play:
            #print("Et un tour de boucle dans la fonction progress InLevel !")
            #print("Premier dialogue.")
            self.fenetre.setFond(self.niveau.fond)
            self.introLevel()
            self.dialoguer(self.niveau.firstDialog)
            #print("On a fini de discuter, première phase de jeu.")
            pygame.mixer.music.load(self.niveau.pathMusicLevel)
            pygame.mixer.music.play(5)
            self.play()
            #print("La première phase est finie, on discute un peu.")
            self.dialoguer(self.niveau.middleDialog)
            #print("Fini de disctuer, place au boss !")
            pygame.mixer.music.load(self.niveau.pathMusicBoss)
            pygame.mixer.music.play(5)
            #ici, ajouter la molécule boss dans la liste des molécules ennemies
            boss = self.niveau.boss
            boss.posX = (constantes.largeur-boss.rect.width)/2
            boss.posY = 10
            boss.rect.x = boss.posX
            boss.rect.y = boss.posY
            self.ennemyList.append(boss)
            self.play()
            pygame.mixer.music.pause()
            #print("On rediscute.")
            self.dialoguer(self.niveau.lastDialog)
            self.outroLevel()

            self.fenetre.selectNextLevel()
            event = pygame.event.wait()
            while 1:
                event = pygame.event.wait()
                if event.type == KEYUP:
                    if event.key == K_RETURN:
                        self.changeNiveau()
                        break
                    elif event.key == K_ESCAPE:
                        play = False
                        break
            pygame.mixer.music.pause()


    def stop(self):
        #si on veut faire des choses particulières une fois qu'on arrête le jeu.
        self.continuer = false

    def changeNiveau(self):
        """Cette fonction s'occupera de charger tout ce dont on a besoin d'un niveau :
            mobs, probas..."""
        #print("Hop, on change de niveau :", str(self.niveau.numero+1))
        self.niveau = Niveau(self.niveau.numero+1)

    def pause(self):
        pause = True
        self.fenetre.afficherPause()
        while pause:
            event = pygame.event.wait()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pause = False
                if event.key == K_r:
                    replay = Replay((constantes.largeur,constantes.hauteur),self.listeFrame)
                    nom = replay.nom
                    replay.saveReplay()


    def clearProj(self):
        for a in self.ennemyProjectiles :
            a.dead = True
        for proj in self.projectilesJoueur:
            proj.dead = True
        """for a in self.ennemyList :
            a.dead = True"""

    def shootJoueur(self):
        projAAjouter = self.typeProjJoueur[self.niveau.numero-1]
        for a in projAAjouter :
                proj = Projectile(a[0]+self.moleculeJoueur.posX,a[1]+self.moleculeJoueur.posY,a[2],a[3])
                proj.img = constantes.projectilesList[0].convert_alpha()
                self.projectilesJoueur.append(proj)
        self.delayTirJoueur=2

    def introLevel(self):
        self.moleculeJoueur.posX = constantes.largeur/2
        self.moleculeJoueur.posY = constantes.hauteur + 10
        x = 0
        for x in range(100):
            self.moleculeJoueur.posY -= 1
            self.actualiser()
            #time.sleep(0.001)
        self.shootJoueur()
        while len(self.projectilesJoueur) > 0:
            for proj in self.projectilesJoueur:
                proj.move()
                if proj.dead:
                    self.projectilesJoueur.remove(proj)
            self.actualiser()

    def outroLevel(self):
        pygame.mixer.music.load('resources/fanfare.wav')
        pygame.mixer.music.play(1)
        self.clearProj()
        self.play()
        self.moleculeJoueur.pattern.mv_y = -5
        self.moleculeJoueur.pattern.mv_x = 0
        while self.moleculeJoueur.dead == False:
            self.moleculeJoueur.move()
            self.actualiser()
        self.moleculeJoueur.dead = False
        self.moleculeJoueur.pattern.mv_y = 0
            #time.sleep(0.001)





