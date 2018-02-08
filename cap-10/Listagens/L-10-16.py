from functools import total_ordering


@total_ordering
class Name:
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name
	
	def __repr__(self):
		return '<Class {3} in 0x{0:x} Name: {1} Key: {2}>'.format(id(self), self.__name, self.__key, type(self).__name__)
	
	def __eq__(self, other):
		print('__eq__ Called')
		return self.name == other.name
	
	def __lt__(self, other):
		print('__lt__ Called')
		return self.name < other.name
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value):
		if value is None or not value.strip():
			raise ValueError('Name can not be null or white!')
		self.__name = value
		self.__key = Name.create_key(value)
	
	@staticmethod
	def create_key(name):
		return name.strip().lower()


o = Name('Thalyson Alexandre Rodrigues de Sousa')
o.name()

print(o.name)

