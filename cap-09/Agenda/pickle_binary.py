from pickle import load, dump

l = []
l1 = [1,2,3, 'thalyson']

arquivo = open('teste', 'wb')

dump(l1, arquivo)

arquivo.close()

arquivo = open('teste', 'rb')

l = load(arquivo)

arquivo.close()

print(l)