import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("""update agenda
                  set telefone = '12345-6789'
                  """)
print("Registros alterados: ", cursor.rowcount)
if cursor.rowcount == 1:
    conexão.commit()
    print("Alterações gravadas")
else:
    conexão.rollback()
    print("Alterações abortadas")
conexão.close()
