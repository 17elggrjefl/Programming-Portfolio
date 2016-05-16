import pygame
import sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Drawing Stuff")

#Palette of colors
BLACK = (  0, 0, 0,)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (  0, 255, 0)
BLUE  = (  0, 0, 255)
RANDOM= (210, 254,  17)

DISPLAYSURF.fill(RANDOM)
pygame.draw.line(DISPLAYSURF, WHITE, (100, 28), (300, 200), 4)
pygame.draw.line(DISPLAYSURF, BLACK, (0, 0), (400, 300), 4)
pygame.draw.line(DISPLAYSURF, BLACK, (0, 300), (400, 0), 4)
pygame.draw.polygon(DISPLAYSURF, RED, ((200,0),(250,50),(225,100),(175,100),(150,50)))
pygame.draw.circle(DISPLAYSURF, BLUE, (275, 140), 48, 0)
pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, 200, 100), 0)
pygame.draw.ellipse(DISPLAYSURF, GREEN, (0, 0, 200, 100), 0)



while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()