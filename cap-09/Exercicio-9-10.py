from sys import argv
from sys import exit

if len(argv) == 1:
	print(argv[0])
	exit(1)
	
saida = open('arq_saida', 'w', encoding='utf-8')

for nome in argv[1:]:
	arquivo = open(nome, encoding='utf-8')
	for linha in arquivo.readlines():
		saida.write(linha)
	arquivo.close()

saida.close()
saida = open('arq_saida', 'r', encoding='utf-8')

for linha in saida.readlines():
	print(linha, end='')

saida.close()