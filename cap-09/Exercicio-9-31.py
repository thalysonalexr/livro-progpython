import os.path

if os.path.isdir('z'):
		print('Z e um diretorio')
elif os.path.isfile('z'):
		print('Z e um arquivo')
else:
	print('Z nao existe')