class Settings():
	def __init__(self):
		"Настройки патрон для корабля"
		self.bullet_speed = 5
		self.bullet_wight = 3
		self.bullet_height = 15
		self.bullet_bg_color = (60, 60, 60)
		self.bullets_allowed = 3
		"Настройка скорости корабля"
		self.ship_speed = 3
		self.ship_limit = 3
		"Настройка самого фона игры"
		self.screen_width = 1200
		self.screen_height = 720
		self.bg_color = (230, 230, 230)
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3.0
		self.alien_speed_factor = 1.0

		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		print(self.alien_points)
