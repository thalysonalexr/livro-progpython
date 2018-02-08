'''from sys import argv
from sys import exit

if len(argv) == 1:
	print(argv[0])
	exit(1)'''
	
nome1 = 'arq_teste.txt'#argv[1]
nome2 = 'saida.txt'#argv[2]
branco = 0

arquivo = open(nome1, encoding='utf-8')
saida = open(nome2, 'w', encoding='utf-8')

for linha in arquivo.readlines():
	if linha == '' or linha == '\n':
		branco += 1
	else:
		branco = 0
	
	if branco < 2:
		palavras = linha.split()
		for i, p in enumerate(palavras):
			if i == (len(palavras)-1):
				saida.write(p)
				break
			saida.write(p + ' ')
		saida.write('\n')
		

arquivo.close()
saida.close()