import sqlite3
from contextlib import closing

with sqlite3.connect('appointment_book.db') as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('select * from appointment_book')
        while True:
            registro = cursor.fetchone()
            if registro is None:
                break
            print('Nome: %s Telefone: %s' % (registro))
