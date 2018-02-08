import os.path
import urllib.request
from sys import argv, exit

formatos = ['.png', '.jpg', '.jpeg']

def carregar_img_html(diretorio):
	pagina = open('imagens.html', 'w', encoding='utf-8')
	pagina.write('''
	<!DOCTYPE html>
	<html lang="pt-BR">
	<head>
	<meta charset="utf-8">
	<title>%Imagens</title>
	</head>
	<body>
	<ul>Arquivos com extensão: {0}</ul>
	'''.format(''.join(formatos)))
	for i, arquivo in enumerate(os.listdir(diretorio)):
		nome, extensao = os.path.splitext(arquivo)
		if extensao in formatos:
			caminho = os.path.join(diretorio, arquivo)
			link = urllib.request.pathname2url(caminho)
			pagina.write("<li>Imagem - %d: <a href='%s'>%s</a></li>" % (i + 1, link, arquivo))
	pagina.write('''
	</body>
	</html>
	''')
	pagina.close()
	
if len(argv) == 1:
	print(argv[0])
	exit(0)

diretorio = argv[1]

if os.path.isdir(diretorio):
	carregar_img_html(diretorio)
elif os.path.isfile(diretorio):
	print('O argumento passado nao e um diretorio.')
else:
	print('Diretorio nao existente.')
	
