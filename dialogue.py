# Créé par Pierre, le 31/03/2016 en Python 3.2
import pygame.image

class Dialog:
    """Classe qui gère les dialogues lors des niveaux."""

    def __init__(self, img1, img2, nom1, nom2):
        self.characters = [[nom1, img1], [nom2, img2]] #La liste des personnages, au cas où il y aurait plus de 2 perso's dans la conversation.
        self.leftPosition = (10, 500)   #Utilisés pour placer les personnages qui parlent sur la fenêtre.
        self.rightPosition = (750, 500)
        self.punchlineList = [] # Une punchline c'est : [réplique(String), indexDuPersoDansLaListeCharacters(int), tupleDePosition(tuple)]
        self.counter = 0
        self.notFinished = True

    def getPunchline(self):
        if counter < len(punchlineList):
            punchline = [self.punchlineList[self.counter][0],
                        self.characters[self.punchlineList[self.counter]][1],
                        self.punchlineList[self.counter][2]]
            self.counter += 1
            if self.counter == len(self.punchlineList):
                notFinished = False
            return punchline
        else:
            return None


