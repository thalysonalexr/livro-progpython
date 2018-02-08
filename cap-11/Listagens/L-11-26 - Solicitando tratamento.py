import sqlite3


with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
    for feriado in conexão.execute("select * from feriados"):
        print(feriado)