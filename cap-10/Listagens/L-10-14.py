class Name:
	def __init__(self, name):
		if name == None or not name.strip():
			raise ValueError('Name can not be null or white!')
		self.name = name
		self.key = name.strip().lower()
		
	def __str__(self):
		return self.name
	
	def __repr__(self):
		return '<Class {3} in 0x{0:x} Name: {1} Key: {2}>'.format(id(self),
		                    self.name, self.key, type(self).__name__)
	
	def __eq__(self, other):
		print('__eq__ Called')
		return self.name == other.name
	
	def __lt__(self, other):
		print('__lt__ Called')
		return self.name < other.name
	

me = Name('Thalyson Alexandre')

print(me)
print(me == Name('Thalyson Alexandre'))
