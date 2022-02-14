import pygame
from settings import *
from debug import draw_text

class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos, group, collision_sprites, enemy):
		super().__init__(group)
		self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
		self.image.fill((255,0,0))
		self.rect  = self.image.get_rect(topleft = pos)

		self.direction = pygame.math.Vector2()
		self.gravity = 0.8
		self.jump = 0

		self.collision_sprites = collision_sprites
		self.enemy = enemy

	def h_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left

	def v_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0
		if self.jump and self.direction.y != 0:
			self.jump = 0
	
	def blow(self):
		for sprite in self.enemy.sprites():	
			if sprite.rect.colliderect(self.rect):	
				if self.rect.top == sprite.rect:
					draw_text("matou", (255, 255, 255), self.display_surface, 20, 20)

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def update(self):
		self.blow()
		self.h_collisions()
		#self.apply_gravity()
		self.v_collisions()