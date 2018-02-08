
LARGURA = 79
entrada = open('entrada.txt')

for linha in entrada.readlines():
	if linha[0] == ';':
		continue
	elif linha[0] == '>':
		print(linha[1:].rjust(LARGURA))
	elif linha[0] == '*':
		print(linha[1:].center(LARGURA))
	elif linha[0] == '=':
		print(linha[0]*40, linha[1:])
	elif linha[0] == '.':
		input("Tecle ENTER para continuar...")
		print()
	else:
		print(linha)
entrada.close()