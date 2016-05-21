# Créé par Baptiste Noblet, le 05/05/2016 en Python 3.2
import pickle
import datetime
import time as _time
from random import *
class Replay:
    def __init__(self,taille,listeFrames) :
        self.taille=taille
        self.listeFrames = listeFrames
        t = _time.time()
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        self.nom = "resources/replay/{1} {0} at {2},{3},{4}.pickle".format(m,d,hh,mm,ss)
    def saveReplay(self) :

        #nom = "resources/replay/{0}_{1}__{2}_{3}_{4}_{5}.pickle".format(datetime.date.month,datetime.date.day,datetime.time.hour,datetime.time.minute,datetime.time.second,datetime.time.microsecond)

        print(self.nom)
        with open(self.nom, 'wb') as file:
            pickle.dump(self,file)

class ReplayLoaded:
    def __init__(self,nom):
        with open(nom, 'rb') as file:
            replay = pickle.load(file)
            self.taille = replay.taille
            self.listeFrames = replay.listeFrames
            self.nom = replay.nom
            print(self.taille)
            print(len(self.listeFrames))