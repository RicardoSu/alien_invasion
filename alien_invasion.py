import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion(object):
	"""Overall class to manage game AlienInvasion"""
	def __init__(self):
		"""Initaialize the game"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption('Alien Invasion')

		self.ship = Ship(self)

	def run_game(self):
		"""Start main game loop"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond for keypress"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()		
			
		pygame.display.flip()




if __name__ == '__main__':
	#Make game instance and run the game
	ai = AlienInvasion()
	ai.run_game()