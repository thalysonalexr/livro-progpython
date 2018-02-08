from os import system
from os import name

agenda = []
atual = None
salvo = True
alterada = False
tipos_telefone = ['celular', 'fixo', 'residencial', 'trabalho', 'fax']



def mostrar_mensagem(mensagem):
	print(mensagem)
	input()


def pede_nome(n='nome do usuario'):
	nome = input("Nome: ").replace('#', '')
	if nome:
		return nome
	return n


def pede_telefone(t='(xx) 1234-5678'):
	telefone = input("Telefone: ").replace('#', '')
	if telefone:
		return telefone
	return t


def cadastra_telefone():
	telefones = []
	while True:
		tipo = mostrar_tipos_telefone()
		telefone = pede_telefone()
		telefones.append([telefone, tipos_telefone[tipo - 1]])
		if not confirmar('Cadastrar outro?'):
			return telefones


def mostrar_tipos_telefone():
	for i, tipo in enumerate(tipos_telefone):
		print('%d - %s |' % (i + 1, tipo), end='')
	return valida_faixa_inteiro('\nTipo: ', 1, 5)


def pede_data_aniversario():
	data = []
	print('Data de aniversario: ')
	dia = valida_faixa_inteiro('Dia: ', 1, 31)
	mes = valida_faixa_inteiro('Mes: ', 1, 12)
	data.append(dia)
	data.append(mes)
	return data


def pede_email(e='exemplo@email.com'):
	email = input('E-mail: ').replace('#', '')
	if email:
		return email
	return e


def pede_nome_arquivo():
	return (input("Nome do arquivo: "))


def mostra_dados(i, nome, dia, mes, email, telefones):
	print("%d - Nome: %s Aniv: %02.d/%02.d E-mail: %s\nTelefones:" % (i, nome, dia, mes, email))
	for t in telefones:
		print('{0:_<25} {1}'.format(t[0], t[1]))
	print()


def valida_faixa_inteiro(pergunta, inicio, fim):
	while True:
		try:
			valor = int(input(pergunta))
			if inicio <= valor <= fim:
				return (valor)
			else:
				print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))
		except ValueError:
			print('Apenas numeros inteiros!')


def confirmar(mensagem=''):
	while True:
		resposta = input(mensagem + ' [s/n]: ').lower()
		if resposta == 's':
			return True
		elif resposta == 'n':
			return False
		else:
			print('Apenas "s" para SIM ou "n" para NÃO!]')


def armazenar_arquivos(nome, quebra):
	arquivo = open('arquivos.txt', 'w', encoding='utf-8')
	try:
		arquivo.write('%s%s' % (nome, quebra))
	except:
		print('Erro! Tente novamente...')
	arquivo.close()


def leitura_arquivos(nome):
	try:
		arquivo = open(nome, encoding='utf-8')
	except FileNotFoundError:
		return None
	return arquivo


def carregar_dados(nome_arquivo):
	global agenda
	agenda = []
	arquivo = leitura_arquivos(nome_arquivo)
	if arquivo is None:
		return None
	for dado in arquivo.readlines():
		telefones = []
		lista = dado.strip().split('#')
		nome = lista[0]
		dia = lista[1]
		mes = lista[2]
		email = lista[3]
		for i in range(4, len(lista), 2):
			telefones.append([lista[i], lista[i+1]])
		agenda.append([nome, [int(dia), int(mes)], email, telefones])
	arquivo.close()


def carregar_ultimo_arquivo():
	global agenda, atual
	arquivo = leitura_arquivos('arquivos.txt')
	if arquivo == None:
		armazenar_arquivos('', '')
		return
	atual = arquivo.readlines()[-1].replace('\n', '')
	arquivo.close()
	if not atual:
		return None
	carregar_dados(atual)


def novo():
	global agenda, alterada, salvo
	nome = pede_nome()
	if pesquisa(nome):
		print('Nome já listado na agenda...')
		return
	telefone = cadastra_telefone()
	data = pede_data_aniversario()
	email = pede_email()
	agenda.append([nome, data, email, telefone])
	mostrar_mensagem('Cadastrado com sucesso!')
	alterada = True
	salvo = False


def apaga():
	global agenda, alterada, salvo
	nome = pede_nome()
	p = pesquisa(nome)
	if p != None:
		if confirmar('Tem certeza que deseja excluir?'):
			del agenda[p]
			mostrar_mensagem('Excluido com sucesso!')
			alterada = True
			salvo = False
		else:
			print("Nome não encontrado.")


def altera():
	global alterada, salvo
	p = pesquisa(pede_nome())
	if p != None:
		nome = agenda[p][0]
		data = agenda[p][1]
		email = agenda[p][2]
		telefone = agenda[p][3]
		print("Encontrado:")
		mostra_dados(p + 1, nome, data[0], data[1], email, telefone)
		nome = pede_nome()
		telefone = cadastra_telefone()
		data = pede_data_aniversario()
		email = pede_email()
		if confirmar('Fazer alteração?'):
			agenda[p] = [nome, data, email, telefone]
			mostrar_mensagem('Alteração bem-sucedida.')
			alterada = True
			salvo = False
	else:
		print("Nome não encontrado.")
		

def pesquisa(nome):
	mnome = nome.lower()
	for p, e in enumerate(agenda):
		if e[0].lower() == mnome:
			return p
	return None


def lista():
	print("\nAgenda\n\n------")
	for i, e in enumerate(agenda):
		mostra_dados(i + 1, e[0], e[1][0], e[1][1], e[2], e[3])
	print("------\n")
	mostrar_mensagem('')


def lê():
	global agenda, alterada
	if alterada:
		if confirmar("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?"):
			grava()
	nome_arquivo = pede_nome_arquivo()
	if carregar_dados(nome_arquivo) == None:
		print('Erro na leitura do arquivo, tente novamente...')
	armazenar_arquivos(nome_arquivo, '\n')
	alterada = False


def grava():
	global alterada, salvo
	if not alterada:
		if not confirmar("Você não alterou a lista. Deseja gravá-la mesmo assim?"):
			return
	nome_arquivo = pede_nome_arquivo()
	arquivo = open(nome_arquivo, "w", encoding="utf-8")
	for e in agenda:
		arquivo.write("%s#%d#%d#%s" % (e[0], e[1][0], e[1][1], e[2]))
		for t in e[3]:
			arquivo.write('#%s#%s' % (t[0], t[1]))
		arquivo.write('\n')
	arquivo.close()
	mostrar_mensagem('Gravado na pastal local!')
	armazenar_arquivos(nome_arquivo, '\n')
	alterada = False
	salvo = True


def salvou():
	if not salvo:
		if confirmar('Deseja salvar alterações feitas em "%s" ?' % atual):
			grava()
		else:
			return
	return None


def ordenar():
	global agenda, alterada, salvo
	agenda.sort(key=lambda e: e[0])
	mostrar_mensagem('Ordenado (A-Z)')
	alterada = True
	salvo = False


def menu():
	system('cls' if name is 'nt' else 'clear')
	print("""
   1 - Novo
   2 - Alterar
   3 - Apagar
   4 - Listar
   5 - Gravar
   6 - Ler arquivo
   7 - Ordenar por nome

   0 - Sair
""")
	print("\nNomes na agenda: %d Alterada: %s\n" % (len(agenda), alterada))
	return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

carregar_ultimo_arquivo() != None

while True:
	opção = menu()
	if opção == 0:
		salvou()
		break
	elif opção == 1:
		novo()
	elif opção == 2:
		altera()
	elif opção == 3:
		apaga()
	elif opção == 4:
		lista()
	elif opção == 5:
		grava()
	elif opção == 6:
		lê()
	elif opção == 7:
		ordenar()