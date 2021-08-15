users = {
			'aeinstien' : {
							'first' : 'albert',
							'last' : 'einstien',
							'location' : 'princeton'
						  },
			'mcurie' : {
							'first' : 'marie',
							'last' : 'curie',
							'location' : 'paris'
						  },
			'ntesla' : {
							'first' : 'nicholas',
							'last' : 'tesla',
							'location' : 'Smiljan'
						  }
		}

for username, user_info in users.items():
	print("\nUsername: " + username)
	print("Full name: " + user_info['first'].title() + " " + user_info['last'].title())
	print("location: " + user_info['location'].title())


for username, user_info in users.items():
	Fname = user_info['first'].title() + " " + user_info['last'].title()
	Loc = user_info['location'].title()
	print("\nUsername: " + username)
	print ("Fullname: " + Fname)
	print ("Location: " + Loc)