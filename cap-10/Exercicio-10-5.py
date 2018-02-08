class Televisao:
	def __init__(self, min=2, max=14):
		self.canal = min
		self.min = min
		self.max = max
	
	def muda_canal_para_baixo(self):
		if self.canal > self.min:
			self.canal -= 1
		else:
			self.canal = self.max
	
	def muda_canal_para_cima(self):
		if self.canal < self.max:
			self.canal += 1
		else:
			self.canal = self.min


tv=Televisao(min=1, max=22)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)

tv2=Televisao(min=2, max=64)
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_cima()
print(tv2.canal)