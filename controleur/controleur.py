# Créé par Pierre, le 09/03/2016 en Python 3.2

import sys
sys.path.append("../modele")
sys.path.append("../vue")

from modele import Modele
from fenetre import Fenetre

class Controleur:
    """La classe du controleur, celle qui fait le lien entre le modele, et l'affichage"""

    def __init__(self, modele, fenetre):
        self.modele = modele
        self.fenetre = fenetre

    def sendToVue(self, molList, molJoueur):
        """Envoie les bonnes images en fonction de l'état des molécules."""
        for mol in molList:
            if mol.isAlive:
                self.fenetre.molecules.append([mol.img, mol.pos])

            else:
                self.fenetre.molecules.append([mol.imgBoum, mol.pos])
        fenetre.rafraichir()