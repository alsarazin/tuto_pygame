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

		self.anim_number = self.anim_inc = 0  # anim_inc needed to avoid changing the image at each update
		self.animation = pygame.image.load("animation.png")
		self.image = self.animation.subsurface((0, 0, 145, 210))
		self.rect = pygame.Rect((50, 200), self.image.get_size())

		self.walking = False

		self.dy = 0  # player's speed in the y axis
		self.jumping = False


	def update(self, dt, game):
		last = self.rect.copy()

		self.walking = False

		# moving player
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and not self.jumping:
			self.dy = -500
			self.jumping = True
		if key[pygame.K_LEFT]:
			self.rect.x -= 300 * dt
			self.walking = True
		if key[pygame.K_RIGHT]:
			self.rect.x += 300 * dt
			self.walking = True

		self.dy = min(400, self.dy+10)
		self.rect.y += self.dy * dt

		# collisions
		new = self.rect
		for cell in pygame.sprite.spritecollide(self, game.walls, False):
			cell = cell.rect
			if last.right <= cell.left and new.right > cell.left:
				new.right = cell.left
			if last.left >= cell.right and new.left < cell.right:
				new.left = cell.right
			if last.bottom <= cell.top and new.bottom > cell.top:
				new.bottom = cell.top
				self.jumping = False
				self.dy = 0
			if last.top >= cell.bottom and new.top < cell.bottom:
				new.top = cell.bottom
				self.dy = 0

		# centered camera
		self.groups()[0].camera_x = self.rect.x - game.width/2
		self.groups()[0].camera_y = self.rect.y - game.height/2

		# walking animation
		if self.walking:
			self.anim_inc += dt*10  # animation depends on time passed (here we have 10 images/sec)
			self.anim_number = int(self.anim_inc) % 7  # there is 8 animation images

			self.image = self.animation.subsurface((145*self.anim_number, 0, 145, 210))  # each image is 145x210

			# needed to stop anim_inc from increasing too much
			if self.anim_inc > 15:
				self.anim_inc = self.anim_inc % 7
			
