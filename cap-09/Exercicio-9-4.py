from sys import argv

def escrever_arquivo(arquivo, arquivo2):
	for linha in arquivo.readlines():
		arquivo2.write('%s' %linha)

if len(argv) == 1:
	print(argv[0])
else:
	nome1 = argv[1]
	nome2 = argv[2]
	
	arq_1 = open(nome1, 'r')
	arq_2 = open(nome2, 'r')
	arq_3 = open('arquivo_gerado.txt', 'w')
	
	escrever_arquivo(arq_1, arq_3)
	escrever_arquivo(arq_2, arq_3)
	
	arq_1.close()
	arq_2.close()
	arq_3.close()