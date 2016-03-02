# Créé par Pierre, le 28/02/2016 en Python 3.2

import pygame
import time

class Fenetre:
    """Classe Fenêtre, s'occupant de l'affichage."""

    def __init__(self, titre, largeur, hauteur):
        pygame.init()
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        self.imgList = []
        pygame.display.set_caption(titre)
        #self.imgList.append(image.load("hakase_nyan.png").convert_alpha())
        #self.fenetre.blit(fond, (0, 0))

    def __del__(self):
        """Possible qu'on n'ait pas à se servir de cette fonction, mais je l'ai créée quand même au cas où."""
        pygame.quit()


    def addImgList(self, img, pos):
        lis = [img, pos]
        self.imgList.append(lis)

    def rafraichir(self):
        #print(self.imgList)
        for lis in self.imgList:
            self.fenetre.blit(lis[0], lis[1])
        pygame.display.flip()

    def fermer(self):
        pygame.quit()


if __name__ == "__main__":
    f = Fenetre("test", 1000, 800)
    f.addImgList(pygame.image.load("hakase_nyan.png").convert_alpha(), (0, 0))
    f.rafraichir();
    time.sleep(2)
    f.fermer()