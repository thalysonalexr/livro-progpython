from sys import argv
from sys import exit

if len(argv) == 1:
	print(argv[0])
	exit(1)

nome = argv[1]

try:
	inicio = int(argv[2])
	fim = int(argv[3])
except:
	print('Please, enter a numbers integer for arguments 2 and 3')
else:
	arquivo = open(nome, encoding='utf-8')
	
	for linha in arquivo.readlines()[(inicio-1):fim]:
		print(linha[:-1])
		
	arquivo.close()