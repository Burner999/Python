def alien_create(aliens , **temp):
	for alien_id in range (30):
		new_alien = {'colour' : 'green', 'points': 5, 'speed': 'slow', 'id' : ((alien_id) + 1)}
		aliens[(alien_id)]=(new_alien)
	return aliens