'''
Created on 31 Jul 2014

@author: alsarazin
'''
import pygame


class Player(pygame.sprite.Sprite):
	'''
	Class that defines the player
	'''

	def __init__(self, *groups):
		'''
		Constructor
		'''
		super(Player, self).__init__(*groups)

		# OLD BABY ZOMBIE IMAGE	
		#self.image = pygame.image.load("zombie.png")
		#self.image = pygame.transform.scale(self.image, (80,80))

		self.anim_number = 0
		self.animation = pygame.image.load("animation.png")

		# TRANSPARENCY NOT SUPPORTED WITH THIS TECHNIQUE
		#self.image = pygame.Surface((145,210))
		#self.image.blit(self.animation, (0, 0), (0, 0, 145, 210))
		
		self.image = self.animation.subsurface((0, 0, 145, 210))

		self.rect = pygame.Rect((50, 200), self.image.get_size())

		self.walking = False

	def update(self, dt, game):
		last = self.rect.copy()

		self.walking = False

		key = pygame.key.get_pressed()
		if key[pygame.K_UP]:
			self.rect.y -= 300 * dt
			self.walking = True
		if key[pygame.K_DOWN]:
			self.rect.y += 300 * dt
			self.walking = True
		if key[pygame.K_LEFT]:
			self.rect.x -= 300 * dt
			self.walking = True
		if key[pygame.K_RIGHT]:
			self.rect.x += 300 * dt
			self.walking = True

		new = self.rect
		for cell in pygame.sprite.spritecollide(self, game.walls, False):
			cell = cell.rect
			if last.right <= cell.left and new.right > cell.left:
				new.right = cell.left
			if last.left >= cell.right and new.left < cell.right:
				new.left = cell.right
			if last.bottom <= cell.top and new.bottom > cell.top:
				new.bottom = cell.top
			if last.top >= cell.bottom and new.top < cell.bottom:
				new.top = cell.bottom

		self.groups()[0].camera_x = self.rect.x - game.width/2
		self.groups()[0].camera_y = self.rect.y - game.height/2

		if self.walking:
			self.anim_number = self.anim_number % 7
			self.anim_number += 1
			self.image = self.animation.subsurface((145*self.anim_number, 0, 145, 210))