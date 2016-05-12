# Créé par Pierre, le 28/02/2016 en Python 3.2

import pygame
import time
import jeu as Jeu
from replay import ReplayLoaded

class Fenetre:
    """Classe Fenêtre, s'occupant de l'affichage."""

    def __init__(self, titre, largeur, hauteur):
        self.fen = pygame.display.set_mode((largeur, hauteur))
        self.largeur = largeur
        self.hauteur = hauteur
        self.font = pygame.font.Font(None, 30)
        #self.imgList = []
        self.entites = [] #une liste qui contient des listes comme ça : [image, tuple_de_position]
        self.fond = None
        pygame.display.set_caption(titre)
        self.explosions = [] #La liste des explosions: [ [ImageExplosion, ListeDeTuplesDePositions] ]
        #self.imgList.append(image.load("hakase_nyan.png").convert_alpha())
        #self.fenetre.blit(fond, (0, 0))
        self.clock = pygame.time.Clock()

    def __del__(self):
        """Possible qu'on n'ait pas à se servir de cette fonction, mais je l'ai créée quand même au cas où."""
        pygame.quit()


    """def addImgList(self, img, pos):
        lis = [img , pos]
        self.imgList.append(lis)"""


    def rafraichir(self, pv):
        #print(self.imgList)
        """for lis in self.imgList:
            self.fen.blit(lis[0], lis[1])"""
        self.fen.blit(self.fond, (0,0))
        for ent in self.entites:
            self.fen.blit(ent.img, (ent.posX, ent.posY))
            #self.fen.fill((255,0,0),ent.rect)    #montre les hitboxs
        for exp in self.explosions:
            #print("On affiche des explosions !")
            for pos in exp[1]:
                self.fen.blit(exp[0], pos)
                #print("Il y a une explosion à :", pos)
        self.clock.tick(60)
        #self.fen.blit(self.font.render(str(self.clock.get_fps()), 1, (180, 180, 255)), (0, 0))
        self.blitLifeBar(pv)
        pygame.display.flip()
        self.entites = []
        self.explosions = []

    def dessinerCadre(self, posX, posY, hauteur, largeur):
        pygame.draw.rect(self.fen, pygame.Color(255, 255, 255, 0), pygame.Rect(posX, posY, largeur, hauteur))

    def ecrireTexte(self, texte, posX, posY):
        """Attention, le texte doit être affiché en dernier, car il faut le flip() 'manuellement'."""
        surface = self.font.render(texte, 0, pygame.Color(255, 0, 0, 0))
        self.fen.blit(surface, (posX, posY))
        pygame.display.flip()

    def fermer(self):
        pygame.quit()

    def afficherPause(self):
        """sombre = pygame.Surface((self.largeur, self.hauteur))
        sombre.set_alpha(128)
        sombre.fill((0, 0, 0))"""
        font = pygame.font.Font(None, 40)
        font2 = pygame.font.Font(None, 20)
        font2.set_italic(True)
        surface = font.render("Pause", 0, pygame.Color(255, 255, 255, 0))
        surface2 = font2.render("Appuyez sur ECHAP pour continuer.", 0, pygame.Color(255, 255, 255, 0))
        surface3 = font2.render("Appuyez sur R pour enregistrer les 15 dernières secondes", 0, pygame.Color(255, 255, 255, 0))
        #self.fen.blit(sombre, (0,0))
        self.assombrir()
        self.fen.blit(surface, ((self.largeur/2)-60, (self.hauteur/2)-40))
        self.fen.blit(surface2, (0, 20))
        self.fen.blit(surface3, (0, 50))
        pygame.display.flip()

    def selectNextLevel(self):
        """sombre = pygame.Surface((self.largeur, self.hauteur))
        sombre.set_alpha(128)
        sombre.fill((0, 0, 0))"""
        font = pygame.font.Font(None, 40)
        font2 = pygame.font.Font(None, 20)
        bravo = font.render("Bravo !", 0, pygame.Color(255, 255, 255, 0))
        choix = font2.render("Appuyez sur ECHAP pour revenir au menu, ENTREE pour continuer.", 0, pygame.Color(255, 255, 255, 0))
        #self.fen.blit(sombre, (0,0))
        self.assombrir()
        self.fen.blit(bravo, ((self.largeur/2)-40, (self.hauteur/2)-50))
        self.fen.blit(choix, ((self.largeur/2) - 200, (self.hauteur/2) + 50))
        pygame.display.flip()


    def playReplay(self,nom):
        replay = ReplayLoaded(nom)
        for a in replay.listeFrames:
            image = pygame.image.frombuffer(a,replay.taille,"RGB")
            self.fen.blit(image, (0,0))
            pygame.display.flip()
            time.sleep(1/60)

    def setFond(self, imgPath):
        self.fond = pygame.image.load(imgPath).convert()
        self.fen.blit(self.fond, (0,0))
        pygame.display.flip()

    def assombrir(self):
        sombre = pygame.Surface((self.largeur, self.hauteur))
        sombre.set_alpha(128)
        sombre.fill((0, 0, 0))
        self.fen.blit(sombre, (0,0))

    def blitLifeBar(self, pv):
        pygame.draw.rect(self.fen, pygame.Color(97, 28, 28, 0), pygame.Rect(10, 10, 100, 20))
        if pv > 0:
            pygame.draw.rect(self.fen, pygame.Color(0, 255, 30, 0), pygame.Rect(10, 10, (pv*100)/20, 20))


    def generiqueFin(self):
        self.setFond("resources/logo.png")

    def selecContinuer(self):
        font = pygame.font.Font(None, 40)
        font2 = pygame.font.Font(None, 20)
        gameOver = font.render("Vous vous êtes fait photopolymériser...", 0, pygame.Color(190, 28, 48, 0))
        continuer = font2.render("Appuyez sur Echap pour quitter, entrée pour réessayer.", 0, pygame.Color(255, 255, 255, 0))
        self.assombrir()
        self.fen.blit(gameOver, ((self.largeur/2)-250, (self.hauteur/2)-50))
        self.fen.blit(continuer, ((self.largeur/2) - 150, (self.hauteur/2) + 50))
        pygame.display.flip()



"""if __name__ == "__main__":
    f = Fenetre("test", 768, 600)
    f.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()
    #f.addImgList(pygame.image.load("hakase_nyan.png").convert_alpha(), (0, 0))
    #f.dessinerCadre(0, 50, 100, 300)
    f.rafraichir()
    #f.ecrireTexte("lel", 500, 200)
    time.sleep(2)
    f.fermer()"""
