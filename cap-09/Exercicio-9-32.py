import os.path
import sys

if len(sys.argv) == 1:
	print(sys.argv[0])
	sys.exit(0)

nome = sys.argv[1]

if os.path.isdir(nome):
		print('Z e um diretorio')
elif os.path.isfile(nome):
		print('Z e um arquivo')
else:
	print('Z nao existe')