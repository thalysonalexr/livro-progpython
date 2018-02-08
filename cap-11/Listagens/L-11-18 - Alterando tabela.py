import sqlite3
from contextlib import closing

with sqlite3.connect('brasil.db') as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('alter table estados add sigla text')
        cursor.execute('alter table estados add região text')