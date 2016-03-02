# Créé par Baptiste Noblet, le 02/03/2016 en Python 3.2

class Atome:

    def __init__(self,hp,x,y) :

        self.hp=hp
        self.x=x
        self.y=y

    def Boom(self) :
        print("Boom la molécule explose !")


class Hydrogene(Atome):
    def __init__(self,hp,x,y):
        self.hp=hp
        self.x=x
        self.y=y