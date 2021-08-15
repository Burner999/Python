aliens = {
			'alien_0' : {
							'colour' : 'green',
							'speed' : 'low',
							'points' : '5'
						  },
			'alien_1' : {
							'colour' : 'yellow',
							'speed' : 'medium',
							'points' : '10'
						  },
			'alien_2' : {
							'colour' : 'red',
							'speed' : 'high',
							'points' : '15'
						  }
		}

for alien, alien_info in aliens.items():
	print("\nColour: " + alien_info['colour'])
	print("Speed: " + alien_info['speed'])
	print("Points: " + alien_info['points'])