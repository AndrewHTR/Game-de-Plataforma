import pygame, sys
from pygame.locals import *
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

level = Level()

while True:
	screen.fill(BG_COLOR)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	level.run()
	pygame.display.update()
	clock.tick(60)