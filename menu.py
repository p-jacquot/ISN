import pygame
from pygame.locals import *

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()



class Menu:
    liste = []
    pola = []
    taille_ecriture = 40
    police_ecriture = 'resources/polices/zawijasy.otf'   #Il faut en trouver une jolie :3 et qui a appelle le dossier ressources avec un s --'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    nombre_d_options = 0
    image_fond = pygame.image.load("resources/fond_transparent.png")
    couleur_texte =  (255, 255, 100)
    couleur_selection = (200,0,100)
    position = 0
    position_affichage = (0,0)
    largeur = 0
    hauteur = 0

    class Zone_menu:
        texte = ''
        zone_menu = pygame.Surface
        zone_rect = pygame.Rect
        selection_rect = pygame.Rect

    def deplacement_menu(self, top, left):
        self.position_affichage = (top,left)

    def set_colors(self, text, selection, background):
        self.image_fond = background
        self.couleur_texte =  text
        self.couleur_selection = selection

    def set_fontsize(self,font_size):
        self.taille_ecriture = font_size

    def set_font(self, path):
        self.police_ecriture = path

    def get_position(self):
        return self.position

    def init(self, liste, dest_surface):
        self.liste = liste
        self.dest_surface = dest_surface
        self.nombre_d_options = len(self.liste)
        self.structure()

    def draw(self,deplacement=0):
        if deplacement:
            self.position += deplacement
            if self.position == -1:
                self.position = self.nombre_d_options - 1                                               #pour se retrouver en bas si tout en haut
            self.position %= self.nombre_d_options
        menu = pygame.Surface((self.largeur, self.hauteur))
        selection_rect = self.pola[self.position].selection_rect
        pygame.draw.rect(menu,self.couleur_selection,selection_rect)

        for i in range(self.nombre_d_options):
            menu.blit(self.pola[i].zone_menu,self.pola[i].zone_rect)
        self.dest_surface.blit(menu,self.position_affichage)
        return self.position

    def structure(self):
        deplacer = 0
        self.hauteur = 0
        self.font = pygame.font.Font(self.police_ecriture, self.taille_ecriture)
        for i in range(self.nombre_d_options):
            self.pola.append(self.Zone_menu())
            self.pola[i].texte = self.liste[i]
            self.pola[i].zone_menu = self.font.render(self.pola[i].texte, 1, self.couleur_texte)

            self.pola[i].zone_rect = self.pola[i].zone_menu.get_rect()
            deplacer = int(self.taille_ecriture * 0.1)                                                      #Taille de chaque cadre

            height = self.pola[i].zone_rect.height
            self.pola[i].zone_rect.left = deplacer
            self.pola[i].zone_rect.top = deplacer+(deplacer*2+height)*i                                    #Espacement entre les options

            width = self.pola[i].zone_rect.width+deplacer*2                                                 #Largeur du cadre
            height = self.pola[i].zone_rect.height+deplacer*2                                               #Hauteur du cadre
            left = self.pola[i].zone_rect.left-deplacer
            top = self.pola[i].zone_rect.top-deplacer

            self.pola[i].selection_rect = (left,top ,width, height)
            if width > self.largeur:
                    self.largeur = width
            self.hauteur += height
        x = self.dest_surface.get_rect().centerx - self.largeur / 2                                         #position x du menu
        y = self.dest_surface.get_rect().centery - self.hauteur / 2                                         #position y du menu
        mx, my = self.position_affichage
        self.position_affichage = (x+mx, y+my)

if __name__ == "__main__":
    import sys

    fenetre = pygame.display.set_mode((1000,880))
    #fond = pygame.image.load("").convert()                                                  #image de fond que je doit faire
    #fenetre.blit(fond, (0,0))
    menu = Menu()
    menu.init(['Nouveau','Continuer','Choix du niveau','Options','Quit'], fenetre)
    menu.draw()
    pygame.key.set_repeat(199,69)
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu.draw(-1)
                if event.key == K_DOWN:
                    menu.draw(1)
                if event.key == K_RETURN:
                    if menu.get_position() == 4:
                        pygame.display.quit()
                        sys.exit()
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()
        pygame.time.wait(8)