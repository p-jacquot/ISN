import pygame
from pygame.locals import *



class Menu :
    liste = []
    pola = []
    taille_ecriture = 40
    police_ecriture = 'resources/polices/zawijasy.otf'   #Il faut en trouver une jolie :3 et qui a appelle le dossier ressources avec un s --'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    couleur_texte =  (255, 255, 100)
    couleur_selection = (200,0,100)
    position = 0
    position_affichage = (10,50)
    largeur = 0
    hauteur = 0

    class Zone_menu:
        texte = ''
        zone_menu = pygame.Surface
        zone_rect = pygame.Rect
        selection_rect = pygame.Rect

    def init(self, liste, dest_surface):
        self.liste = []
        self.pola = []
        self.taille_ecriture = 40
        self.police_ecriture = 'resources/polices/zawijasy.otf'   #Il faut en trouver une jolie :3 et qui a appelle le dossier ressources avec un s --'
        self.font = pygame.font.Font
        self.dest_surface = pygame.Surface
        self.couleur_texte =  (255, 255, 100)
        self.couleur_selection = (200,0,100)
        self.position = 0
        self.position_affichage = (10,50)
        self.largeur = 0
        self.hauteur = 0
        self.liste = liste
        self.dest_surface = dest_surface
        self.nombre_d_options = len(self.liste)
        self.structure()

    def deplacement_menu(self, top, left):
        self.position_affichage = (top,left)

    def set_colors(self, text, selection):
        self.image_fond = background
        self.couleur_texte =  text
        self.couleur_selection = selection

    def set_fontsize(self,font_size):
        self.taille_ecriture = font_size

    def set_font(self, path):
        self.police_ecriture = path

    def get_position(self):
        return self.position

    def draw(self,deplacement=0):
        if deplacement:
            self.position += deplacement
            if self.position == -1:
                self.position = self.nombre_d_options - 1                                               #pour se retrouver en bas si tout en haut
            self.position %= self.nombre_d_options
        menu = pygame.Surface((self.largeur, self.hauteur))
        menu = pygame.image.load( "resources/photos/fond transparent.png" ).convert()
        selection_rect = self.pola[self.position].selection_rect
        for i in range(self.nombre_d_options):
            self.pola[i].zone_menu= self.font.render(self.pola[i].texte,1,self.couleur_texte)
        for i in range(self.position+1):
            self.pola[self.position].zone_menu= self.font.render(self.pola[self.position].texte,1,self.couleur_selection)
            if self.position==0:
                self.pola[0].zone_menu= self.font.render(self.pola[0].texte,1,self.couleur_selection)
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

