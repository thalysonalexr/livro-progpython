from sys import argv
from sys import exit

if len(argv) == 1:
	print(argv[0])
	exit(1)

nome = argv[1]
arquivo = open(nome, encoding='utf-8')

for linha in arquivo.readlines():
	print(linha, end='')
	
arquivo.close()