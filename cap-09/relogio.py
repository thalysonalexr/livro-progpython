import os
import time
import modulo_hora_atual

while True:
	hora = modulo_hora_atual.mostrar_horario()
	print(hora)
	time.sleep(1)
	os.system('cls' if os.name is 'nt' else 'clear')