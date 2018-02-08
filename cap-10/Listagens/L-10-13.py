class OnlyList():
	def __init__(self, elem_class):
		self._list = []
		self.elem_class = elem_class
		
	def __len__(self):
		return len(self._list)
	
	def __iter__(self):
		return iter(self._list)
	
	def __getitem__(self, item):
		return self._list[item]
	
	def invalid_index(self, i):
		return i >= 0 and i < len(self._list)
	
	def add(self, elem):
		if self.search(elem) == -1:
			self._list.append(elem)
	
	def remove(self, i):
		if self.search(i) != -1:
			self._list.pop(i)
	
	def search(self, elem):
		self.check_type(elem)
		try:
			return self._list.index(elem)
		except ValueError:
			return -1
		
	def check_type(self, elem):
		if type(elem) != self.elem_class:
			raise TypeError('Tipo invalido')
		
	def sort(self, key=None):
		self._list.sort(key=key)
		
row = OnlyList(int)
for i in range(10):
	row.add(i)

for e in row:
	print(end='{0}, '.format(e))