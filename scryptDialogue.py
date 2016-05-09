# Créé par Baptiste Noblet, le 09/05/2016 en Python 3.2
import pickle
from dialogue import Dialog
niveau = int(input("dialogue pour quel niveau ?"))
place = int(input("quelle est la place de ce dialogue ? 0 pour le début, 1 pour avant le boss et 2 pour apres le boss"))

personnageGauche = str(input("Nom du personnage à gauche"))
personnageDroite = str(input("Nom du personnage à droite"))
dialogue = Dialog("resources/temporaire/{}.png".format(personnageGauche),personnageGauche,(10,210),"resources/temporaire/{}.png".format(personnageDroite),personnageDroite,(500,200))

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