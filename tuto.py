#!/usr/bin/python
'''
Created on 30 Jul 2014

@author: alsarazin
'''
import pygame
from player import Player


class ScrolledGroup(pygame.sprite.Group):
	def draw(self, surface):
		for sprite in self.sprites():
			surface.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y - self.camera_y))


class Game(object):
	'''
	Class that defines the game in itself
	'''

	def main(self, screen):

		self.width, self.height = 640, 480

		clock = pygame.time.Clock()

		background = pygame.image.load("background.png")

		level_width, level_height = background.get_size()

		sprites = ScrolledGroup()
		sprites.camera_x = 0
		sprites.camera_y = 0
		self.player = Player(sprites)
		
		self.walls = pygame.sprite.Group()
		block = pygame.image.load('block.png')

		for x in range(0, self.width+32*20, 32):
			for y in range(0, self.height+32*4, 32):
				if x in (0, self.width + 32*20 - 32) or y in (0, self.height +32*4 - 32):
					wall = pygame.sprite.Sprite(self.walls)
					wall.image = block
					wall.rect = pygame.Rect((x, y), wall.image.get_size())
		sprites.add(self.walls)

		while True:
			dt = clock.tick(40)  # amount of time in ms that passed since the last tick was called

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return
					elif event.key == pygame.K_s:
						rail.play()

			screen.fill((255,255,255))
			sprites.update(dt / 1000., self)
			screen.blit(background, (-416 - sprites.camera_x, -400 - sprites.camera_y))
			sprites.draw(screen)
			pygame.display.flip()


if __name__ == '__main__':
	pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
	pygame.init()
	try:
		#pygame.mixer.music.load(os.path.join('data', 'an-turr.ogg'))#load music
		#jump = pygame.mixer.Sound(os.path.join('data','jump.wav'))  #load sound
		#fail = pygame.mixer.Sound(os.path.join('data','fail.wav'))  #load sound
		rail = pygame.mixer.Sound('raygun-01.wav')  #load sound
	except:
		print("could not load or play soundfiles in 'data' folder :-(")

	screen = pygame.display.set_mode((640, 480))
	Game().main(screen)

