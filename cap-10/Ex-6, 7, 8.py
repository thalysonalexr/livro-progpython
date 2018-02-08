class Banco:
	def __init__(self, nome):
		self.nome = nome
		self.contas = []
		
	def abre_conta(self, conta):
		self.contas.append(conta)
		
	def lista_contas(self):
		for c in self.contas:
			c.resumo()
	
class Cliente:
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone


class Conta:
	def __init__(self, clientes, numero, saldo=0):
		self.saldo = 0
		self.clientes = clientes
		self.numero = numero
		self.operacoes = []
		self.deposito(saldo)
	
	def resumo(self):
		print('CC Numero: %s Saldo: %10.2f' % (self.numero, self.saldo))
		print('Dono(s): --------- Contato:')
		for cliente in self.clientes:
			print('%s --------- %s' % (cliente.nome, cliente.telefone))
			
	def pode_sacar(self, valor):
		return self.saldo >= valor
	
	def saque(self, valor, mensagem='Saldo insuficiente!'):
		if self.pode_sacar(valor):
			self.saldo -= valor
			self.operacoes.append(['SAQUE', valor])
		else:
			print(mensagem)
	
	def deposito(self, valor):
		self.saldo += valor
		self.operacoes.append(['DEPOSITO', valor])
	
	def extrato(self):
		print('Extrato CC N° %s\n' % self.numero)
		for o in self.operacoes:
			print('%10s %10.2f' % (o[0], o[1]))
		print('\n Saldo: %10.2f\n' % self.saldo)


class ContaEspecial(Conta):
	def __init__(self, clientes, numero, saldo=0, limite=0):
		Conta.__init__(self, clientes, numero, saldo)
		self.limite = limite
	
	def pode_sacar(self, valor):
		return (self.saldo + self.limite) >= valor
			
	def extrato(self):
		Conta.extrato(self)
		print('Saldo disponivel: %10.2f\nLimite do saldo: %10.2f\n' % (self.saldo + self.limite, self.limite))


joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joão], 1, 1000)
conta2 = ContaEspecial([maria, joão], 2, 500, 1000)

bancotatu = Banco('Tatu')
bancotatu.abre_conta(conta1)
bancotatu.abre_conta(conta2)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1895.15)

conta1.extrato()
conta2.extrato()

print('Banco %s\n' % bancotatu.nome)
bancotatu.lista_contas()