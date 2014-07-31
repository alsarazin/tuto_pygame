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
		clock = pygame.time.Clock()

		sprites = pygame.sprite.Group()
		self.player = Player(sprites)

		while True:
			dt = clock.tick(40)  # amount of time in ms that passed since the last tick was called

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return

			sprites.update(dt / 1000.)
			screen.fill((255, 255, 255))
			sprites.draw(screen)
			pygame.display.flip()


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Game().main(screen)
