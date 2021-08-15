active='TRUE'
print(active)
current_number = 1
while active=='TRUE':
	while current_number <=5:
		print(current_number)
		current_number +=1
		if current_number == 5:
			print(current_number)
			active='FALSE'
			break
print("FLAG value changed from (TRUE) to (FALSE), exiting program")
	

