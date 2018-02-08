import sqlite3
from contextlib import closing

print('Região Número de Estados')
print('========================')
with sqlite3.connect('brasil.db') as conn:
    with closing(conn.cursor()) as cursor:
        for região in cursor.execute('select região, count(*) from estados group by região'):
            print("{0:6} {1:17}".format(*região))