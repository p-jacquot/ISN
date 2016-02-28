# Créé par Pierre, le 28/02/2016 en Python 3.2
from Fenetre import *
import time

f = Fenetre("test", 1000, 800)
f.rafraichir()
time.sleep(5)
f.fermer()