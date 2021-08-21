class Car():
	"""A simple attempt to model a car"""

	def __init__ (self, make, model, year, colour, odometer_reading):
		"""initialize name and age"""
		self.make = make
		self.model = model
		self.year = year
		self.colour = colour
		self.odometer_reading = odometer_reading

	def description(self):
		print("This car is a " + self.year + " " + self.make.title() + " " + self.model)

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " KMs on it")

	def update_odometer(self, newmileage):

		if self.odometer_reading < newmileage:
			self.odometer_reading = newmileage
			self.description()
			self.read_odometer()
	
		elif mycar.odometer_reading == newmileage:
			print("No change to mileage")

		else:
			print("You can't rollback the mileage !")
			
			

mycar = Car('BMW' ,'3 Series Coupe' , '2007' , 'Silver' , '176659' )
mycar.description()
mycar.read_odometer()
msg=("Is the above mileage correct ? (y/n)")
conf=input(msg)

if conf == 'n':
	newmsg=("Enter mileage:")
	newmileage=input(newmsg)
	mycar.update_odometer(newmileage)
else:
	print("Enjoy your new car !")
	









