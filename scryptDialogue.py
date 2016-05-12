# Créé par Baptiste Noblet, le 09/05/2016 en Python 3.2
import pickle
from dialogue import Dialog
niveau = int(input("dialogue pour quel niveau ?"))
place = int(input("quelle est la place de ce dialogue ? 0 pour le début, 1 pour avant le boss et 2 pour apres le boss"))

personnageGauche = str(input("Nom du personnage à gauche"))
imagePersonnageGauche = str(input("quelle est l'image du personnage de gauche ? sans l'extension s'il vous plait"))
personnageDroite = str(input("Nom du personnage à droite"))
imagePersonnageDroite = str(input("quelle est l'image du personnage de droite ? sans l'extension s'il vous plait"))
dialogue = Dialog("resources/personnages/{}.png".format(imagePersonnageGauche),personnageGauche,(10,210),"resources/personnages/{}.png".format(imagePersonnageDroite),personnageDroite,(500,200))

nombrePunchline = int(input("quel est le nombre de punchline au total ?"))
for a in range(nombrePunchline):
    quote = str(input("quelle est la phrase numéro {}".format(a+1)))
    perso = int((input("qui le dit ? 0 pour le personnage de gauche et 1 pour la droite")))
    dialogue.punchlineList.append([quote,perso])


if place == 0 :
    nom = "first"
elif place == 1 :
    nom = "middle"
elif place == 2 :
    nom = "last"
nom="resources/niveau/"+str(niveau)+"/"+nom+"Dialog.pickle"

with open(nom, 'wb') as file:
    pickle.dump(dialogue, file)