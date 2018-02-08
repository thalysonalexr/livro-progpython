from sys import argv
from sys import exit

if len(argv) == 1:
	print(argv[0])
	exit(1)

nome = argv[1]
arquivo = open(nome, encoding='utf-8')

dic = {}
l = 1
c = 1

for linha in arquivo.readlines():
	linha = linha.strip().lower()
	palavras = linha.split(' ')
	for palavra in palavras:
		if palavra == '':
			c += 1
			continue
		if palavra in dic:
			dic[palavra].append((l, c))
		else:
			dic[palavra]=[(l, c)]
		c = len(palavra) + 1
	l += 1
	c = 1
		
arquivo.close()

for chave in dic:
	print('{0} : {1}'.format(chave, dic[chave]))