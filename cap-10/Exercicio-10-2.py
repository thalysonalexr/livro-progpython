class Televisao:
	def __init__(self, canal, min, max):
		self.canal = canal
		self.min = min
		self.max = max
	
	def muda_canal_para_baixo(self):
		if self.canal > self.min:
			self.canal -= 1
			
	def muda_canal_para_cima(self):
		if self.canal < self.max:
			self.canal += 1
	
		     
tv=Televisao(1, 1, 3)

print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)