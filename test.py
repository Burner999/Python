aliens = {}
count = 0
while count in range (30):
	alien_id = count + 1
	# dynamically create key
	alien_inv = 'alien_' + str(alien_id)
	# calculate value
	value = {'colour' : 'green', 'points': 5, 'speed': 'slow', 'id' : (alien_id)}
	aliens[alien_inv] = value
	count += 1
print(aliens)
