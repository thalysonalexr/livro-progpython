import sqlite3

conn = sqlite3.connect('appointment_book.db')
cursor = conn.cursor()

dados = [('Matheus Henrique Sea', '66-332343233'),
         ('Mariane Tedesco Espinola', '12-332131233'),
         ('Julia Martins Farias', '44-31323145566')]



cursor.executemany('''
    insert into appointment_book (name, phone) values(?, ?)
''', dados)

conn.commit()
cursor.close()
conn.close()
