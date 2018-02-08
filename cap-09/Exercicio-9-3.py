def leia_numero(arquivo):
	numero = arquivo.readline()
	while True:
		if numero is '':
			return None
		if numero.strip() != '':
			return int(numero)
		

def escrever_numero(arquivo, n):
	arquivo.write('%d\n' %n)
	

pares = open('pares.txt', 'r')
impar = open('impares.txt', 'r')
par_impar = open('imp_par.txt', 'w')

n_par = leia_numero(pares)
n_imp = leia_numero(impar)

while True:
	if n_par is None and n_imp is None:
		break
	if n_par != None and (n_imp == None or n_par <= n_imp):
		escrever_numero(par_impar, n_par)
		n_par = leia_numero(pares)
		
	if n_imp != None and (n_par == None or n_imp <= n_par):
		escrever_numero(par_impar, n_imp)
		n_imp = leia_numero(impar)

pares.close()
impar.close()
par_impar.close()