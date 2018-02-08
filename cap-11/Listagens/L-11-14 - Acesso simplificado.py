import sqlite3

with sqlite3.connect("agenda.db") as conexão:
    for registro in conexão.execute("select * from agenda"): #<1>
        print("Nome: %s\nTelefone: %s" % (registro))
