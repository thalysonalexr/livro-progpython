pares = open('pares.txt', 'r')
novo = open('novo_pares.txt', 'w')

lista = pares.readlines()

for i in range(len(lista)-1, -1, -1):
	novo.write(lista[i])
	
pares.close()
novo.close()