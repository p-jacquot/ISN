import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
while 1:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			Haut = pygame.event.get()       #il faut que je fasse afficher la valeur!!!!!
			print(Haut)
