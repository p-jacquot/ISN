# Créé par Pierre, le 05/03/2016 en Python 3.2

from vue.fenetre import Fenetre

class Modele:
    """La classe qui s'occupera de gérer le jeu en lui même"""

    def __init__(self, fenetre, niveau): #on lui donnera le niveau qu'on veut jouer (un int, et on ira chercher dans des dossiers).
        self.fenetre = fenetre
        self.changeNiveau(niveau)
        self.ennemyList = []
        self.continuer = false
        self.moleculeJoueur = Atome()  #bon ok, c'est un atome...

    def play(self):
        while self.continuer:
            #La boucle principale du jeu.
            print("yolo ! On s'amuse bien !")

    def stop(self):
        #si on veut faire des choses particulières une fois qu'on arrête le jeu.
        self.continuer = false

    def changeNiveau(self, niveau):
        """Cette fonction s'occupera de charger tout ce dont on a besoin d'un niveau :
            mobs, probas..."""
        self.niveau = niveau




