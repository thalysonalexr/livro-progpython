import sqlite3

conn = sqlite3.connect('appointment_book.db')
cursor = conn.cursor()

try:
    cursor.execute('''
        create table appointment_book(
            name text,
            phone text)
    ''')
except sqlite3.OperationalError:
    print('Tabela já criada...')

name = input('Enter your name: ')
phone = input('Phone: ')

cursor.execute('''
    insert into appointment_book(name, phone)
        values(?, ?)
''', (name, phone))

conn.commit()
cursor.close()
conn.close()
