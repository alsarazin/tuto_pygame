'''
Created on 31 Jul 2014

@author: alsarazin
'''

import pygame
import os


class Player(pygame.sprite.Sprite):
	'''
	Class that defines the player
	'''

	zombie_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "zombie.jpg")

	def __init__(self, *groups):
		'''
		Constructor
		'''
		super(Player, self).__init__(*groups)
		self.image = pygame.image.load(self.zombie_path)
		self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

	def update(self, dt, game):
		last = self.rect.copy()

		key = pygame.key.get_pressed()
		if key[pygame.K_UP]:
			self.rect.y -= 300 * dt
		if key[pygame.K_DOWN]:
			self.rect.y += 300 * dt
		if key[pygame.K_LEFT]:
			self.rect.x -= 300 * dt
		if key[pygame.K_RIGHT]:
			self.rect.x += 300 * dt

		for __cell in pygame.sprite.spritecollide(self, game.walls, False):
			self.rect = last
