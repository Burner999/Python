aliens = []

for alien_id in range (30):
	new_alien = {'colour' : 'green', 'points': 5, 'speed': 'slow', 'id' : (alien_id) + 1}
	aliens.append(new_alien)

for alien in aliens[:5]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['colour'] == 'yellow':
		alien['colour'] = 'red'
		alien['speed'] = 'high'
		alien['points'] = 15 

#for alien in aliens[5:10]:
#	if alien['colour'] == 'green':
#		alien['colour'] = 'red'
#		alien['speed'] = 'high'
#		alien['points'] = 15

for alien in aliens[:30]:
	print(alien)
print ("...")
print ("Total number of aliens: " +str(len(aliens)))