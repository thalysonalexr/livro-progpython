import sqlite3

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
    conexão.row_factory = sqlite3.Row
    for feriado in conexão.execute("select * from feriados"):
        print("{0} {1}".format(feriado["data"].strftime("%d/%m/%y"), feriado["descrição"]))