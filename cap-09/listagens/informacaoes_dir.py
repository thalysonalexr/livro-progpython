import os.path
import time
nome = 'avô'
print("Nome: %s" % nome)
print("Tamanho: %d" % os.path.getsize(nome))
print("Criado: %s" % time.ctime(os.path.getctime(nome)))
print("Modificado: %s" % time.ctime(os.path.getmtime(nome)))
print("Acessado: %s" % time.ctime(os.path.getatime(nome)))