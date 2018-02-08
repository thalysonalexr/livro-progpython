class Televisao:
	def __init__(self, canal, min=2, max=14):
		self.canal = canal
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


tv = Televisao(12)

print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)