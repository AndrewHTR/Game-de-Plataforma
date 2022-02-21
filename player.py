import pygame
from settings import *
from debug import draw_text
class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group, collision_sprites, enemy, coin):
		super().__init__(group)
		# Setando animação e sprite do jogador
		self.images = []
		self.images.append(pygame.image.load('sprite/player/player.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/player/player_1.png').convert_alpha())
		self.images.append(pygame.image.load('sprite/player/player_2.png').convert_alpha())
		
		self.index = 0
		self.image = self.images[self.index]
		self.rect  = self.image.get_rect(topleft = pos)

		self.anima = False

		# Movimento do Player
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.jump = 0

		self.moedas = 0
		self.pontuacao = 0

		self.collision_sprites = collision_sprites
		self.enemy = enemy
		self.coin = coin


	# Input das teclas e movimento do jogador
	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.direction.x = 1
			#self.anima = True

		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.direction.x = -1 
			#self.anima = True

		else:self.direction.x = 0
		
		if keys[pygame.K_SPACE] and self.jump == 1:
			self.direction.y = -self.jump_speed
			self.pressing_space = True
			#self.jump += 1
			draw_text("Pulou", (255, 255, 255), pygame.display.get_surface(), 120, 20)


	# Colisão do jogador com o mapa
	def h_collisions(self):
		keys = pygame.key.get_pressed()
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
					
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left

	def v_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				self.passed_time = 0
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.jump = 1

				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0
				draw_text("chão", (255, 255, 255), pygame.display.get_surface(), 120, 20)

		if self.jump and self.direction.y != 0:
			self.jump = 0

	# Colisão do jogador com o inimigo
	def h_collisions_enemy(self):
		for sprite in self.enemy.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.direction.x = 0
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.direction.x = 0
					self.rect.right = sprite.rect.left

	def v_collisions_enemy(self):
		for sprite in self.enemy.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top 
					self.direction.y = 0
					self.jump = 1


				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0
					draw_text("inimigo", (255, 255, 255), pygame.display.get_surface(), 120, 20)


	# Função para matar inimigo caso o player pule em cima dele
	def blow(self):
		keys = pygame.key.get_pressed()
		for sprite in self.enemy.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:

					self.jump = 1
					draw_text("colidiu matar", (255, 255, 255), pygame.display.get_surface(), 120, 20)
					#self.rect.bottom = sprite.rect.top	
					if keys[pygame.K_SPACE] and self.jump == 1:
						self.direction.y = -self.jump_speed
					sprite.kill()
					self.pontuacao += 100


    # Adicionar gravidade ao jogador
	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y 


	# Trocar sprite caso a condição seja atendida
	def change(self):
		for image in self.images:
			if self.direction.x < 0:
				self.image = pygame.transform.flip(image, True , False)
				#self.anima = True

			if self.direction.x > 0:
				self.image = pygame.transform.flip(image, False , False)
				#self.anima = True

	# Colisão com moedas 
	def coins(self):
		for sprite in self.coin.sprites():
			if sprite.rect.colliderect(self.rect):
				sprite.kill()
				self.moedas += 1


	# Atualização por frame do jogador
	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.h_collisions()
		self.h_collisions_enemy()
		self.apply_gravity()
		self.blow()
		self.v_collisions_enemy()
		self.v_collisions()
		self.change()
		self.coins()

		if self.anima == True:
			self.index += 0.08

			if self.index >= len(self.images):
				self.index = 0
				self.anima = False

			self.image = self.images[int(self.index)]
		draw_text(f"Moedas: {str(f'{self.moedas}')}", (255, 255, 255), pygame.display.get_surface(), 20, 40)
		draw_text(f"Pontuação: {str(f'{self.pontuacao}')}", (255, 255, 255), pygame.display.get_surface(), 20, 60)