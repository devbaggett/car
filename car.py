# assignment name and separator
print "\n----------Assignment: Car----------\n"

# create class: 'car', where user can specify its attributes
class Car(object):
	# this method to run every time a new object is instantiated
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12

	# displays the info of the car in console
	def displayInfo(self):
		print "Price: ${}".format(self.price)
		print "Speed: {}mph".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Mileage: {} miles".format(self.mileage)
		print "Tax rate: {}%".format(self.tax * 100)

# create 6 instances of class: 'cars'
car1 = Car(1000, 50, "Full", 15)
car2 = Car(5000, 80, "Almost Full", 20)
car3 = Car(10000, 100, "Half Full", 25)
car4 = Car(20000, 140, "Half Empty", 22)
car5 = Car(30000, 160, "Almost Empty", 16)
car6 = Car(50000, 200, "on 'E'", 14)

# car separator/border
print "\n-----Car 1-----"
# displays car's attributes
car1.displayInfo()
print "\n-----Car 2-----"
car2.displayInfo()
print "\n-----Car 3-----"
car3.displayInfo()
print "\n-----Car 4-----"
car4.displayInfo()
print "\n-----Car 5-----"
car5.displayInfo()
print "\n-----Car 6-----"
car6.displayInfo()

# bottom separator/border
print ""