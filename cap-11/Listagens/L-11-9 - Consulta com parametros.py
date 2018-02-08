import sqlite3

nome=input("Nome a selecionar: ")
conexão = sqlite3.connect("precos.db")
cursor = conexão.cursor()
cursor.execute('select * from precos where prod_nome = ?', (nome,))
x=0
while True:
    resultado=cursor.fetchone()
    if resultado == None:
        if x == 0:
            print("Nada encontrado.")
        break
    print("Nome: %s\nPreco: %s" % (resultado))
    x+=1
cursor.close()
conexão.close()