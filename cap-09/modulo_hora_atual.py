import time

def dia_semana():
	inf = time.localtime()
	dias = {0:'Segunda', 1:'Terça', 2:'Quarta', 3:'Quinta', 4:'Sexta', 5:'Sabádo', 6:'Domingo'}
	chave = inf.tm_wday
	return dias[chave]+'-feira'
	
	
def mes():
	inf = time.localtime()
	meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
	         7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
	chave = inf.tm_mon
	return meses[chave]


def mostrar_horario(divisor=':'):
	h, m, s = horario()
	hora = str(h) + divisor + str(m) + divisor + str(s)
	return hora


def horario():
	inf = time.localtime()
	return inf.tm_hour, inf.tm_min, inf.tm_sec

def data():
	inf = time.localtime()
	return inf.tm_mday, inf.tm_mon, inf.tm_year


def mostrar_data_abrev(divisor='/'):
	d, m, a = data()
	return str('%02.d%s%02.d%s%02.d' %(d, divisor, m, divisor, a))
	

def mostrar_data_completa(divisor='/'):
	d, m, a = data()
	stringmes = mes()
	sem = dia_semana()
	return str('%02.d%s%s%s%02.d - %s' %(d, divisor, stringmes, divisor, a, sem))

	
