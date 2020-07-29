import pygame

class Ship(object):
	"""Am class for the Ship"""
	def __init__(self, ai_game):
		"""Ship and starting possition"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#load ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Star each ship at the bottom center
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Draw ship at current location"""
		self.screen.blit(self.image,self.rect)