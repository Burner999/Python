alien_0 ={'colour': 'green', 'points': 5, 'speed': 'medium', 'scratch': 999}

print (alien_0['colour'])
print (alien_0['points'])

new_points = alien_0['points']
alien_0['x_position'] = 0
alien_0['y_position'] = 25


alien_1={}
alien_1['colour'] = 'yellow'
alien_1['points'] = 10
alien_1['x_position'] = 10
alien_1['y_position'] = 25
alien_1['speed'] = 'high'



print("You scored " + str(new_points) + " points!")
print ("alien_0 = " + str(alien_0))
print ("alien_1 = " + str(alien_1))

print("Alien_0 Original X position= " +str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("Alien_0 new X position= " +str(alien_0['x_position']))
print("Alien_0 scratch val= " +  str(alien_0['scratch']))
print(alien_0)
del alien_0['scratch']
print(alien_0)