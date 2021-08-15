active='TRUE'
print("Current flag value is " + active)
current_number = 0
while active != 'FALSE':
	current_number +=1
	if current_number == 5:
		active='FALSE'
		print(current_number)
		continue
	print(current_number)
print("FLAG value changed from TRUE to " + active + " , exiting program")
	

