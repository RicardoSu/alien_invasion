import settings

class GameStats:
	"""docstring for GameStats"""
	def __init__(self, ai_game):

		self.settings = ai_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""Initializr statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
		