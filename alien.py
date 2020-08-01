import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to manage Bullets from the Ship"""
	def __init__(self,ai_game):
		"""Create a bullet object at the ship current possition"""

		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#load the alien image and set rect atribute
		self.image = pygame.image.load('images/alien_grey.bmp')
		self.rect = self.image.get_rect()

		#Start each alien at top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store th alien exact horozontal possition

		self.x = float(self.rect.x)

	def _update_aliens(self):
		"""Move the alien to the right"""
		self.x += self.settings.alien_speed
		self.rect.x = self.x

	def check_edges(self):
		
		