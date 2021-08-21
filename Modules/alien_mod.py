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