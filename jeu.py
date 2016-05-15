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
        self.moleculeJoueur.hpMax = 20
        self.moleculeJoueur.hp = 20
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
        if self.niveau.numero < len(self.typeProjJoueur) :
            self.projAAjouter = self.typeProjJoueur[self.niveau.numero-1]
        else :
            self.projAAjouter = self.typeProjJoueur[-1]
        #self.moleculeJoueur = Atome()  #bon ok, c'est un atome...
        self.framesInvincibilite = 0

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
                self.moleculeJoueur.hit(1)
                print(self.moleculeJoueur.dead)
                explosion1.play()
                self.ennemyList[indexMechant].hit(3)
                #self.clearProj()

            indexMechantProjectile = self.moleculeJoueur.rect.collidelist(epr)
            if self.framesInvincibilite > 0 :
                self.framesInvincibilite-= 1

            if indexMechantProjectile != -1 and self.framesInvincibilite == 0:
                self.moleculeJoueur.hit(1)
                print(self.moleculeJoueur.dead)
                explosion1.play()
                self.ennemyProjectiles[indexMechantProjectile].dead=True #On supprime le projectile, s'il a touché sa cible.
                self.framesInvincibilite = 50
                #self.clearProj()

            for proj in self.projectilesJoueur:
                index = proj.rect.collidelist(er)
                if index != -1:
                    self.ennemyList[index].hit(3)
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

            self.delayTirJoueur -= 1
            if self.tir == True and self.delayTirJoueur <=0 :
                self.shootJoueur()


            if self.niveau.totalMobsLeft <= 0 and len(self.ennemyList) <= 0:
                self.continuer = False
            elif self.moleculeJoueur.dead:
                self.continuer = False
                self.niveau.totalMobsLeft = 0
                self.ennemyList = []

            self.moleculeJoueur.move()
            if self.moleculeJoueur.dying:
                self.fenetre.explosions.append(self.moleculeJoueur.explodeCoords)
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
        if self.framesInvincibilite/2 == int(self.framesInvincibilite/2) :
            self.fenetre.entites.append(self.moleculeJoueur)
        self.fenetre.rafraichir(self.moleculeJoueur.hp)

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
            if p[2][0] == 500 :
                p[2]= (constantes.largeur-rect.width,self.fenetre.hauteur-100-rect.height)
        while dialog.notFinished:
            punchline = dialog.getPunchline()
            posX, posY = perso[punchline[1]][2]

            #print(punchline[1][0])
            #pygame.draw.rect(self.fenetre.fen, pygame.Color(0, 0, 0, 0), pygame.Rect(0, 0, self.fenetre.largeur, self.fenetre.hauteur))
            self.fenetre.rafraichir(self.moleculeJoueur.hp)
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
            self.fenetre.setFond(self.niveau.fond)
            self.introLevel()
            self.dialoguer(self.niveau.firstDialog)
            pygame.mixer.music.load(self.niveau.pathMusicLevel)
            pygame.mixer.music.play(5)
            self.play()

            if self.moleculeJoueur.dead == False:
                self.dialoguer(self.niveau.middleDialog)
                pygame.mixer.music.load(self.niveau.pathMusicBoss)
                pygame.mixer.music.play(5)
                boss = self.niveau.boss
                boss.posX = (constantes.largeur-boss.rect.width)/2
                boss.posY = 10
                boss.rect.x = boss.posX
                boss.rect.y = boss.posY
                self.ennemyList.append(boss)
                self.play()
                pygame.mixer.music.pause()
            if self.moleculeJoueur.dead == False:
                self.dialoguer(self.niveau.lastDialog)
                self.outroLevel()

                constantes.niveauActuel = self.niveau.numero+1
                if constantes.niveauMaxFait < constantes.niveauActuel :
                    constantes.niveauActuel = 1
                    constantes.sauvegarder()
                    self.niveau.numero = 0
                    self.fenetre.generiqueFin()
                if constantes.niveauActuel>constantes.niveauMaxAtteint :
                    constantes.niveauMaxAtteint = constantes.niveauActuel
                constantes.sauvegarder()

                self.fenetre.selectNextLevel()
                key = self.waitForSelection()
                if key == K_RETURN:
                    self.changeNiveau(1) #on lui donne 1 quand on veut le niveau suivant.
                    break
                elif key == K_ESCAPE:
                    play = False
                    break
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.load("resources/game_over.wav")
                pygame.mixer.music.play(1)
                self.fenetre.selecContinuer()
                key = self.waitForSelection()
                if key == K_ESCAPE:
                    play = False
                elif key == K_RETURN:
                    self.moleculeJoueur.reset()
                    self.clearProj()
                    self.ennemyList = []
                    self.play()
                    self.changeNiveau(0) #Et 0 quand on recharge le niveau.
                    pygame.mixer.music.pause()

    def waitForSelection(self):
        while 1:
            event = pygame.event.wait()
            if event.type == KEYUP:
                if event.key == K_RETURN or event.key == K_ESCAPE:
                    return event.key

    def stop(self):
        #si on veut faire des choses particulières une fois qu'on arrête le jeu.
        self.continuer = false

    def changeNiveau(self, plus):
        """Cette fonction s'occupera de charger tout ce dont on a besoin d'un niveau :
            mobs, probas..."""
        #print("Hop, on change de niveau :", str(self.niveau.numero+1))
        self.niveau = Niveau(self.niveau.numero + plus)
        if self.niveau.numero < len(self.typeProjJoueur) :
            self.projAAjouter = self.typeProjJoueur[self.niveau.numero-1]
        else :
            self.projAAjouter = self.typeProjJoueur[-1]

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
        for a in self.projAAjouter :
                proj = Projectile(a[0]+self.moleculeJoueur.posX,a[1]+self.moleculeJoueur.posY,a[2],a[3])
                proj.img = constantes.projectilesList[0].convert_alpha()
                self.projectilesJoueur.append(proj)
        self.delayTirJoueur=2

    def introLevel(self):
        self.framesInvincibilite = 0
        self.moleculeJoueur.posX = constantes.largeur/2
        self.moleculeJoueur.posY = constantes.hauteur + 10
        self.moleculeJoueur.pattern.mv_x = 0
        self.moleculeJoueur.pattern.mv_y = -1
        x = 0
        for x in range(100):
            self.moleculeJoueur.move()
            self.actualiser()
            #time.sleep(0.001)
        self.moleculeJoueur.pattern.mv_y = 0

        self.shootJoueur()
        while len(self.projectilesJoueur) > 0:
            for proj in self.projectilesJoueur:
                proj.move()
                if proj.dead:
                    self.projectilesJoueur.remove(proj)
            self.actualiser()

    def outroLevel(self):
        self.framesInvincibilite = 0
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





