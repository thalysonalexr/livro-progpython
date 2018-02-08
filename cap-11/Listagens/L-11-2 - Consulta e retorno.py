import sqlite3

conn = sqlite3.connect('appointment_book.db')
cursor = conn.cursor()

cursor.execute('select * from appointment_book')
data = cursor.fetchall()

for e in data:
    print('Nome %s Telefone: %s' % (e))


cursor.close()
conn.close()

input()