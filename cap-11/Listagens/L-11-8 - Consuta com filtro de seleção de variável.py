import sqlite3

nome=input("Nome a selecionar: ")
conexão = sqlite3.connect("precos.db")
cursor = conexão.cursor()
cursor.execute('select * from precos where prod_nome = "%s"' % nome)
while True:
    resultado=cursor.fetchone() #<1>
    if resultado == None:
        break
    print("Nome: %s\nPreco: %.2f" % (resultado)) #<2>
cursor.close()
conexão.close()

# exemplo de SQLInjection nesse programa X" or "1"="1