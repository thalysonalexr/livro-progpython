# Método fetchone melhor para não obter uma grande lista ocupando memória por fetchall

import sqlite3

conn = sqlite3.connect('appointment_book.db')
cursor = conn.cursor()
cursor.execute('select * from appointment_book')

while True:
    registro = cursor.fetchone()
    if registro is None:
        break
    print('Nome: %s Telefone: %s' % (registro))

cursor.close()
conn.close()
