class Televisao:
	def __init__(self):
		self.ligada = False
		self.canal = 0
		self.tamanho = 0.0
		self.marca = None
		
	def __str__(self):
		return str('%s, %d, %.1f, %s' % (self.ligada, self.canal, self.tamanho, self.marca))


tv1 = Televisao()
tv2 = Televisao()

tv1.ligada = True
tv1.canal = 3
tv1.tamanho = 21.5
tv1.marca = 'Samsung'

tv2.ligada = False
tv2.canal = 7
tv2.tamanho = 51.5
tv2.marca = 'Phillips'

print(tv1.__str__())
print(tv2.__str__())