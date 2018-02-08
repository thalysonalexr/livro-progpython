import sqlite3

with sqlite3.connect("brasil.db") as conexão:
    for feriado in conexão.execute("select * from feriados"):
        print(feriado)