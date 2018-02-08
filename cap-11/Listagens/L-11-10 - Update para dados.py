import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("""update agenda
                  set telefone = '12345-6789'
                  where nome = 'Nilo'""")
conexão.commit()
conexão.close()