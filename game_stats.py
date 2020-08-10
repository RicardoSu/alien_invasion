class GameStats:
	"""docstring for GameStats"""
	def __init__(self, ai_game):

		self.settings = ai_game.settings
		self.reset_stats()

		#Start Alien Invasion in an inactive state
		self.game_active = False




	def reset_stats(self):
		"""Initializr statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0

	#Start game in an inactive state



		