#!/usr/bin/python

import pygame, os

class Game(object):
	
	def main(self, screen):
		clock = pygame.time.Clock()
		
                zombie_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "zombie.jpg")

		zombie = pygame.image.load(zombie_path)
		zombie_x, zombie_y = 320, 240		
		
		while True:
			clock.tick(40)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_ESCAPE:
						return
			
			key = pygame.key.get_pressed()
			if key[pygame.K_UP]:
				zombie_y -= 10
			if key[pygame.K_DOWN]:
				zombie_y += 10
			if key[pygame.K_LEFT]:
				zombie_x -= 10
			if key[pygame.K_RIGHT]:
				zombie_x += 10		
			
			screen.fill((255,255,255))
			screen.blit(zombie,(zombie_x, zombie_y))
			pygame.display.flip()
 

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	Game().main(screen)

