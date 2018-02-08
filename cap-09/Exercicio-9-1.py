import sys

if len(sys.argv) == 1:
     print(sys.argv[0])
else:
     nome = sys.argv[1]
     arquivo = open(nome, "r")
     for linha in arquivo.readlines():
          print(linha[:-1])

     arquivo.close()