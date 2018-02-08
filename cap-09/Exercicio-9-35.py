import sys
import os.path
import urllib.request


def gerar_pagina_html(nomedir, arquivo):
	pagina.write('''
	<!DOCTYPE html>
	<html lang="pt-BR">
	<head>
	<meta charset="utf-8">
	<title>Exercicio-9.35</title>
	</head>
	<body>
	<ul>Arquivos encontrados a partir do diretorio: %s</ul>
	''' % nomedir)
	for raiz, subdir, arquivos in os.walk(nomedir):
		for a in arquivos:
			caminho = os.path.join(raiz, a)
			link = urllib.request.pathname2url(caminho)
			pagina.write('<p><li><a href="%s">%s</a>(Bytes: %d)</li></p>' % (link, a, os.path.getsize(link)))
	pagina.write('''
	</body>
	</html>
	''')
	pagina.close()


if len(sys.argv) == 1:
	sys.exit(0)
	
try:
	nomedir = sys.argv[1]
except IndexError:
	print('Apenas um diretorio como parametro!')
	sys.exit(0)

pagina = open('PaginaHTML.html', 'w', encoding='utf-8')

gerar_pagina_html(nomedir, pagina)