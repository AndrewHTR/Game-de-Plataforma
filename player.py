import pygame
from settings import *
from debug import draw_text
class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group, collision_sprites):
		super().__init__(group)
		self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
		self.image.fill(PLAYER_COLOR)
		self.rect  = self.image.get_rect(topleft = pos)

		# Movimento do Player
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.jump = 0

		self.collision_sprites = collision_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1 
		else:self.direction.x = 0
		if keys[pygame.K_SPACE] and self.jump == 1:
			self.direction.y = -self.jump_speed
			#self.jump += 1
			draw_text("Pulou", (255, 255, 255), pygame.display.get_surface(), 20, 20)

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
					self.jump = 1

				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0

		if self.jump and self.direction.y != 0:
			self.jump = 0

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y 

	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.h_collisions()
		self.apply_gravity()
		self.v_collisions()