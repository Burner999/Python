aliens = {}
count = 0

class Alien():
	"""A simple class for creating aliens in the game"""

	def __init__(self,alien_id,colour,speed,points):
		self.id = alien_id
		self.colour = colour
		self.speed = speed
		self.points = points
		#self.x_coord = x_coord
		#self.y_coord = y_coord

def alien_display(aliens):
	for alien, alien_info in aliens.items():
		print("\n")
		print("ID: " + str(alien_info['alien_id']))
		print("Colour: " + alien_info['colour'])
		print("Speed: " + alien_info['speed'])
		print("Points: " + str(alien_info['points']))
	return aliens

def alien_mod(aliens):
	for alien_id, alien_atts in aliens.items():
		count = alien_id
		if count <= 4:
			if alien_atts['colour'] == 'green':
				alien_atts['colour'] = 'yellow'
				alien_atts['speed'] = 'medium'
				alien_atts['points'] = 10
			elif alien_atts['colour'] == 'yellow':
				alien_atts['colour'] = 'red'
				alien_atts['speed'] = 'high'
				alien_atts['points'] = 15
	return aliens

aliens = {}
count = 0

while count in range (30):
	alien_id = count + 1
	# dynamically create key
	alien_inv = 'alien_' + str(alien_id)
	# calculate value
	value = { 'alien_id' : (alien_id), 'colour' : 'green', 'speed': 'slow', 'points': 5}
	aliens[alien_inv] = Alien(value)
	print("Generated Alien: " + new.alien_id + ' ' + new.colour + ' ' + new.speed + ' ' + new.points )
	count += 1



#aliens = alien_mod(aliens)

#alien_display(aliens)

#aliens = alien_mod(aliens)

#alien_display(aliens)
