class Cat():
	"""A simple attempt to model a dog"""

	def __init__ (self, name, age):
		"""initialize name and age"""
		self.name = name
		self.age = age

	def description(self):
		print(self.name.title() + " is " + str(self.age) + " years old")

	def scratch(self):
		print(self.name.title() + " is scratching the couch again")

	def sleep(self):
		print(self.name.title() + " is sleeping in the cat bed")

	def snobbish(self):
		print(self.name.title() + " doesn't like the cat food in the bowl")

mycat = Cat('Daisy',12)
mycat.description()
mycat.scratch()
mycat.sleep()
mycat.snobbish()

mumscat = Cat('Rosie',10)
mumscat.description()
mumscat.scratch()
mumscat.sleep()
mumscat.snobbish()




