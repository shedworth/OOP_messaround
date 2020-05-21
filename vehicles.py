from mixins import Flying
from schedulable import Schedulable

class Vehicle(Schedulable):

	def __init__(self, **kwargs):
		self.__engine_size = kwargs['engine_size'] if 'engine_size' in kwargs.keys() else self.default_engine_size()
		self.post_initialise(**kwargs)

	def default_engine_size(self):
		raise NotImplementedError

	def post_initialise(self, **kwargs):
		pass

	def spares(self):
		return {'fuel': self.engine_size*5, **self.local_spares()}

	def local_spares(self):
		return {}

	def lead_days(self):
		return 1

	# Getters and setters
	@property
	def engine_size(self):
		return self.___engine_size
	
	@engine_size.setter
	def engine_size(self, engine_size):
		self.__engine_size = engine_size





class LandVehicle(Vehicle):

	def post_initialise(self, **kwargs):
		self.__seats = kwargs['seats']
		self.__doors = kwargs['doors']

	def default_engine_size(self):
		return 2.0

	#Getters and setters
	@property
	def seats(self):
		return self.__seats

	@property
	def doors(self):
		return self.__doors
	
	@seats.setter
	def seats(self, seats):
		self.__seats = seats

	@doors.setter
	def doors(self, doors):
		self.__doors = doors





class Car(Flying, LandVehicle):

	def __repr__(self):
		return "Car with {0} seats".format(self.seats)

	def local_spares(self):
		return {	'spare tyre': 1,
							'oil':				1,
							}




class Van(LandVehicle):

	def post_initialise(self, **kwargs):
		self.__wheelbase = kwargs['wheelbase']

	def __repr__(self):
		return "{0} wheelbase van with {1} seats".format(self.wheelbase, self.seats)

	#Getters and setters
	@property
	def wheelbase(self):
		return self.__wheelbase
	
	@wheelbase.setter
	def wheelbase(self, wheelbase):
		self.__wheelbase = wheelbase





class Boat(Vehicle):

	def post_initialise(self, **kwargs):
		self.__berth = kwargs['berth']
		self.__beam = kwargs['beam']

	def __repr__(self):
		return "{0} berth boat".format(self.berth)

	def local_spares(self):
		return {'life jacket': self.berth}

	def lead_days(self):
		return 5

	#Getters and setters
	@property
	def berth(self):
		return self.__berth

	@property
	def beam(self):
		return self.__beam
	
	@berth.setter
	def berth(self, berth):
		self.__berth = berth

	@beam.setter
	def beam(self, beam):
		self.__beam = beam





class Tank(LandVehicle):

	def post_initialise(self, **kwargs):
		self.__main_gun 		= kwargs['main_gun']
		self.__machine_guns = kwargs['machine_guns']

	def local_spares(self):
		return {	'bullets': 5000, 
							'shells': 20,
						}

	#Getters and setters
	@property
	def main_gun(self):
		return self.__main_gun
	
	@main_gun.setter
	def main_gun(self, calibre):
		self.__main_gun = calibre
