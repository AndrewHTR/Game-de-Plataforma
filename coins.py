import pygame
from settings import *
from debug import draw_text
class Coins(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.images = []
		self.images.append(pygame.image.load('sprite/coins/coin.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/coins/coin_1.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/coins/coin_2.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/coins/coin_3.png').convert_alpha())

		
		self.index = 0
		self.image = self.images[self.index]
		self.rect  = self.image.get_rect(topleft = pos) 

	def update(self):
		self.index += 0.14

		if self.index >= len(self.images):
				self.index = 0
				

		self.image = self.images[int(self.index)]