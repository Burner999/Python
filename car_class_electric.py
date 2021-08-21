class Car():
	"""A simple attempt to model a car"""

	def __init__ (self, make, model, year, colour, odometer_reading):
		"""initialize name and age"""
		self.make = make
		self.model = model
		self.year = year
		self.colour = colour
		self.odometer_reading = odometer_reading
		self.category = 'combustion'

	def description(self):
		print("This car is a " + self.year + " " + self.make.title() + " " + self.model)

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " KMs on it")

	def update_odometer(self, newmileage):

		if self.odometer_reading < int(newmileage):
			self.odometer_reading = int(newmileage)
			self.description()
			self.read_odometer()
	
		elif mycar.odometer_reading == newmileage:
			print("No change to mileage")

		else:
			print("You can't rollback the mileage !")

class ElectricCar(Car):
	"""Represents aspects of an electric car"""
	def __init__(self, make, model, year, colour, odometer_reading, charge_level):
		super().__init__(make, model, year, colour, odometer_reading)
		self.charge_level = charge_level
		self.category = 'electric'

	def charging(self):

		if (int(self.charge_level) < 100) and (int(self.charge_level) > 50):
			print("You're car has enough charge")
		elif (int(self.charge_level) <= 50) and (int(self.charge_level) > 20):
			print("You should consider charging your car soon")
		else:
			print("You need to charge your car soon")

	def update_charge_level(self, new_charge_level):
		self.charge_level = new_charge_level
						

mycar = ElectricCar('Porsche' ,'Taycan' , '2021' , 'Chalk' , 0 , 80 )
mycar.description()
mycar.read_odometer()
mycar.charging()

if mycar.category == 'electric':
	msg=("Your charge level is " + str(mycar.charge_level) + "%." + " Is this correct ? (y/n)" )
	conf=input(msg)
	if conf == 'n':
		newmsg=("Enter charge_level:")
		new_charge_level=input(newmsg)
		mycar.update_charge_level(new_charge_level)
		mycar.charging()

msg=("Is the above mileage correct ? (y/n)")
conf=input(msg)
if conf == 'n':
	newmsg=("Enter mileage:")
	newmileage=input(newmsg)
	mycar.update_odometer(newmileage)
else:
	print("Enjoy your new car !")
	









