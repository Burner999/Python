active='TRUE'
print("Current flag value is " + active)
current_number = 1
while True:
	print(current_number)
	current_number +=1
	if current_number == 5:
		print(current_number)
		active='FALSE'
		break
print("FLAG value changed from TRUE to " + active + " , exiting program")
	

