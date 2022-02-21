import pygame
from settings import *
from debug import draw_text

class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.images = []
		self.images.append(pygame.image.load('sprite/enemy/slime.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/enemy/slime_1.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/enemy/slime_2.png').convert_alpha())
		#self.images.append(pygame.image.load('enemy/slime_1.png').convert_alpha())
		#self.images.append(pygame.image.load('enemy/slime_2.png').convert_alpha())
		#self.images.append(pygame.image.load('enemy/slime.png').convert_alpha())


		
		self.index = 0
		self.image = self.images[self.index]
		self.rect  = self.image.get_rect(topleft = pos)

		self.direction = pygame.math.Vector2()
		self.gravity = 0.8
		self.speed = 8
		self.jump = 0		
	
	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def update(self):
		#self.apply_gravity()
		#self.rect.x += self.direction.x * self.speed
		self.index += 0.03

		if self.index >= len(self.images):
				self.index = 0
				self.anima = False

		self.image = self.images[int(self.index)]