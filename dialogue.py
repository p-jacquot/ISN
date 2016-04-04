# Créé par Pierre, le 31/03/2016 en Python 3.2
import pygame.image

class Dialog:
    """Classe qui gère les dialogues lors des niveaux."""

    def __init__(self, img1, nom1, pos1, img2, nom2, pos2):
        self.characters = [[nom1, img1, pos1], [nom2, img2, pos2]] #La liste des personnages, au cas où il y aurait plus de 2 perso's dans la conversation.
        #pos1 et pos2 sont des tuples de position !
        #print(self.characters)
        #self.leftPosition = (10, 100)   #Utilisés pour placer les personnages qui parlent sur la fenêtre.
        #self.rightPosition = (500, 100)
        self.punchlineList = [] # Une punchline c'est : [réplique(String), indexDuPersoDansLaListeCharacters(int)]
        self.counter = 0
        self.notFinished = True

    def getPunchline(self):
        if self.counter < len(self.punchlineList):
            punchline = [self.punchlineList[self.counter][0],
                        self.characters[self.punchlineList[self.counter][1]][0],
                        self.characters[self.punchlineList[self.counter][1]][1],
                        self.characters[self.punchlineList[self.counter][1]][2]]
            self.counter += 1
            if self.counter >= len(self.punchlineList):
                self.notFinished = False
            return punchline
        else:
            return None


