import sqlite3

conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute("""select * from precos where prod_nome = "Amaciante Omo" """)
while True:
    resultado=cursor.fetchone() #<1>
    if resultado == None:
        break
    print("Nome: %s\nPreco: %s" % (resultado)) #<2>
cursor.close()
conexao.close()