def alien_display(aliens):
	for alien, alien_info in aliens.items():
		print("\n")
		print("ID: " + str(alien_info['id']))
		print("Colour: " + alien_info['colour'])
		print("Speed: " + alien_info['speed'])
		print("Points: " + str(alien_info['points']))