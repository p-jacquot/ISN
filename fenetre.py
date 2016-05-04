# Créé par Pierre, le 28/02/2016 en Python 3.2

import pygame
import time
import jeu as Jeu

class Fenetre:
    """Classe Fenêtre, s'occupant de l'affichage."""

    def __init__(self, titre, largeur, hauteur):
        self.fen = pygame.display.set_mode((largeur, hauteur))
        self.largeur = largeur
        self.hauteur = hauteur
        self.font = pygame.font.Font(None, 30)
        #self.imgList = []
        self.entites = [] #une liste qui contient des listes comme ça : [image, tuple_de_position]
        #self.fond = fond
        pygame.display.set_caption(titre)
        self.explosions = [] #La liste des explosions: [ [ImageExplosion, ListeDeTuplesDePositions] ]
        #self.imgList.append(image.load("hakase_nyan.png").convert_alpha())
        #self.fenetre.blit(fond, (0, 0))

    def __del__(self):
        """Possible qu'on n'ait pas à se servir de cette fonction, mais je l'ai créée quand même au cas où."""
        pygame.quit()


    """def addImgList(self, img, pos):
        lis = [img , pos]
        self.imgList.append(lis)"""


    def rafraichir(self):
        #print(self.imgList)
        """for lis in self.imgList:
            self.fen.blit(lis[0], lis[1])"""
        self.fen.blit(self.fond, (0,0))
        for ent in self.entites:
            self.fen.blit(ent.img, (ent.posX, ent.posY))
            self.fen.fill((255,0,0),ent.rect)    #montre les hitboxs
        for exp in self.explosions:
            #print("On affiche des explosions !")
            for pos in exp[1]:
                self.fen.blit(exp[0], pos)
                #print("Il y a une explosion à :", pos)


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

"""if __name__ == "__main__":
    f = Fenetre("test", 768, 600)
    f.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()
    #f.addImgList(pygame.image.load("hakase_nyan.png").convert_alpha(), (0, 0))
    #f.dessinerCadre(0, 50, 100, 300)
    f.rafraichir()
    #f.ecrireTexte("lel", 500, 200)
    time.sleep(2)
    f.fermer()"""
