import pygame
from settings import *
from tile import Tile
from player import Player
from enemy import Enemy
from coins import Coins

class Level:

	def __init__(self):
		# Level setup
		self.display_surface = pygame.display.get_surface()

		# Sprite group setup
		self.visible_sprites   = CameraGroup()
		self.active_sprites    = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()
		self.enemy 			   = pygame.sprite.Group()
		self.coin  			   = pygame.sprite.Group()
		self.setup_level()

	def setup_level(self):
		for yindex, row in enumerate(LEVEL_MAP):
			for xindex, col in enumerate(row):
				x = xindex * TILE_SIZE
				y = yindex * TILE_SIZE
				if col == "X":
					Tile((x, y), [self.visible_sprites, self.collision_sprites])
				if col == 'P':
					self.player = Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites, self.enemy, self.coin)
				if col == 'E':
					Enemy((x, y + 42), [self.visible_sprites, self.active_sprites, self.enemy])
				if col == 'C':
					Coins((x,y - 15), [self.visible_sprites,self.active_sprites, self.coin])

	def reset(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_r]:
			pass


	def run(self):
		# Roda o level 
		self.active_sprites.update()
		self.enemy.update()
		self.visible_sprites.custom_draw(self.player)
		#self.reset()

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		#self.offset 		 = pygame.math.Vector2(100, 300)

		# center camera setup
		#self.half_w = self.display_surface.get_size()[0] // 2
		#self.half_h = self.display_surface.get_size()[1] // 2

		# camera box
		cam_left   = CAMERA_BORDERS['left']
		cam_top    = CAMERA_BORDERS['top']
		cam_width  = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS['right'])
		cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS['bottom'])

		self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)


	def custom_draw(self, player):

		# get player offset
		#self.offset.x = player.rect.centerx - self.half_w
		#self.offset.y = player.rect.centery - self.half_h

		# pegando posição da camera
		if player.rect.left < self.camera_rect.left:
			self.camera_rect.left = player.rect.left

		if player.rect.right > self.camera_rect.right:
			self.camera_rect.right = player.rect.right
			
		if player.rect.top < self.camera_rect.top:
			self.camera_rect.top = player.rect.top

		if player.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = player.rect.bottom

				#
		# camera offset
		self.offset = pygame.math.Vector2(self.camera_rect.left - CAMERA_BORDERS['left'], 
										  self.camera_rect.top - CAMERA_BORDERS['top'])
		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)