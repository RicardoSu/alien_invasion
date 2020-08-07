import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion(object):
	"""Overall class to manage game AlienInvasion"""
	def __init__(self):
		"""Initaialize the game"""
		pygame.init()
		self.settings = Settings()

		#Screen windows mode
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))

		#Makes full screen but ship slower

		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height



		pygame.display.set_caption('Alien Invasion')

		#Create instance to store game statistics
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		#Look for aliens-ship collisions


		self._create_fleet()



	def _create_fleet(self):
		"""Create the fleet of aliens"""
		#create an alien and find the number of aliens ina row
		#spacing between each alien is equal to one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 *alien_width)
		number_aliens_x = (available_space_x //(2 * alien_width))

		#determine the number of rows of aliens that fit on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
							(3 * alien_height) - ship_height)
		number_rows = (available_space_y // (2 * alien_height)) - 2  

		#create the full flet of aliens

		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)


	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)


	def _check_fleet_edges(self):
		"""Respond appropiately if anyaliens have reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_droop_speed
		self.settings.fleet_direction *= -1


	def run_game(self):
		"""Start main game loop"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
			self._update_aliens()
			


			
	def _update_bullets(self):
		"""Update  position of bullets and get tid of the old ones"""	
		#Update bullet possitions
		self.bullets.update()

		#Get rid of old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)


		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):

		"""Respond t bullet-alien colisions"""	

		#Check forany bullets that have hit aliens
		#if so get hit of the bullet and the alien

		collisions= pygame.sprite.groupcollide(
			self.bullets, self.aliens, False, True)

		if not self.aliens:
			#Destroy existing bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()		

	def _check_events(self):
		"""Respond for keypress"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""Respond for key presses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		#WASD keyborad to play

		elif event.key == pygame.K_d:
			self.ship.moving_right = True
		elif event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_w:
			self.ship.moving_up = True
		elif event.key == pygame.K_s:
			self.ship.moving_down = True



		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond for key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_UP:
			self.ship.moving_up = False	
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False

		#WASD cursor

		if event.key == pygame.K_d:
			self.ship.moving_right = False
		if event.key == pygame.K_a:
			self.ship.moving_left = False
		if event.key == pygame.K_w:
			self.ship.moving_up = False	
		if event.key == pygame.K_s:
			self.ship.moving_down = False



	def _fire_bullet(self):
		"""Create a new bullet and add it to the group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)		
		pygame.display.flip()


	def _update_aliens(self):
		"""
		Check if the fleet is at an edge,
			then update the positions of all aliens in the fleet
		"""
		self._check_fleet_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()

	def _ship_hit(self):
		"""Respond to the ship beinghit by an alien"""		
		#Decrement ships left
		self.stats.ships_left -= 1

		#get rid of  any remaining aliensand bulets
		self.aliens.empty()
		self.bullets.empty()

		#create a new fleet and center ship

		self._create_fleet()
		self.ship.center_ship()

		#Pause
		sleep(0.5)





if __name__ == '__main__':
	#Make game instance and run the game
	ai = AlienInvasion()
	ai.run_game()