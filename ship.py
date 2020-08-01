import pygame

class Ship(object):
	"""Am class for the Ship"""
	def __init__(self, ai_game):
		"""Ship and starting possition"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#load ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Start each ship at the bottom center
		self.rect.midbottom = self.screen_rect.midbottom

		#store adecimal value for the ship horizontal possition
		self.x = float(self.rect.x)

		#store a decimal value for the ship vertical position
		self.y = float(self.rect.y)

		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship position based on the movement flag"""
		#Update the ship x value not the rect 
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0 :
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0 :
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
			self.y += self.settings.ship_speed
		#Update rect object from self.x
		self.rect.x = self.x
		#Update rect object from self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw ship at current location"""
		self.screen.blit(self.image,self.rect)