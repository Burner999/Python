def counter(current_number):
	"""increments current number counter"""
	current_number +=1
	return current_number

def flag(active):
	active='FALSE'
	return active

current_number = 0
active='TRUE'
print("Current flag value is " + active)
while active != 'FALSE':
	current_number = counter(current_number)
	if current_number == 5:
		active = flag(active)
		print(current_number)
		continue
	print(current_number)
print("FLAG value changed from TRUE to " + active + " , exiting program")