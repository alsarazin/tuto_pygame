'''
Created on 30 Jul 2014

@author: alsarazin
'''
#!/usr/bin/python

import pygame
from player import Player


class Game(object):
	'''
	Class that defines the game in itself
	'''

	def main(self, screen):

		width, height = 640, 480

		clock = pygame.time.Clock()

		background = pygame.image.load("background.png")

		sprites = pygame.sprite.Group()
		self.player = Player(sprites)

		self.walls = pygame.sprite.Group()
		block = pygame.image.load('block.png')

		for x in range(0, width, 32):
			for y in range(0, height, 32):
				if x in (0, width - 32) or y in (0, height - 32):
					wall = pygame.sprite.Sprite(self.walls)
					wall.image = block
					wall.rect = pygame.rect.Rect((x, y), wall.image.get_size())
		sprites.add(self.walls)

		while True:
			dt = clock.tick(40)  # amount of time in ms that passed since the last tick was called

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return

			sprites.update(dt / 1000., self)
			screen.blit(background, (0, 0))
			sprites.draw(screen)
			pygame.display.flip()


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Game().main(screen)
