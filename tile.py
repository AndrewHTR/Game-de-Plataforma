import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill(TILE_COLOR)
		self.rect  = self.image.get_rect(topleft = pos) 