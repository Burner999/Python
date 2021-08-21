def alien_mod( aliens):
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

def alien_create(aliens , **temp):
	for alien_id in range (30):
		new_alien = {'colour' : 'green', 'points': 5, 'speed': 'slow', 'id' : ((alien_id) + 1)}
		aliens[(alien_id)]=(new_alien)
	return aliens

def alien_display(aliens):
	for alien, alien_info in aliens.items():
		print("\n")
		print("ID: " + str(alien_info['id']))
		print("Colour: " + alien_info['colour'])
		print("Speed: " + alien_info['speed'])
		print("Points: " + str(alien_info['points']))

aliens = {}
test = {'test_text': 'test'}

aliens = alien_create(aliens)

aliens = alien_mod(aliens)

alien_display(aliens)

aliens = alien_mod(aliens)

alien_display(aliens)





	

