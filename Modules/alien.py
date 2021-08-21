count = 0

def alien_create(aliens):
	for alien_id in range (30):
		new_alien = { 'id' : ((alien_id) + 1) ,'colour' : 'green', 'points': 5, 'speed': 'slow' }
		aliens[(alien_id)]=(new_alien)
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

def alien_display(aliens):
	for alien_id, alien_atts in aliens.items():
		print("\n")
		print("ID: " + str(alien_atts['id']))
		print("Colour: " + alien_atts['colour'])
		print("Speed: " + alien_atts['speed'])
		print("Points: " + str(alien_atts['points']))
	return aliens

