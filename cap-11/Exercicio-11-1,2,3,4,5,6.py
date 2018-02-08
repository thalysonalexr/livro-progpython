import sqlite3
from contextlib import closing


def create_table(name):
    try:
        with sqlite3.connect('Prices.db') as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('''
                    create table %s(
                        prod_id integer primary key autoincrement,
                        prod_name text,
                        prod_price float)
                ''' % name)
    except sqlite3.OperationalError:
        print('Table prices exists.')


def insert_products(products):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.executemany('insert into prices(prod_name, prod_price) values (?, ?)', (products))


def consult_all_table(table):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from %s' % table)
            while True:
                register = cursor.fetchone()
                if register is None:
                    break
                print('Product: %s Price %.2f R$' % register[1:])


def search_price(name, table, message='Not found.'):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from %s where prod_name = ?' % table, (name,))
            qtd = 0
            while True:
                register = cursor.fetchone()
                if register is None:
                    if qtd == 0:
                        print(message)
                    break
                print('Product: %s Price: %.2f R$' % register[1:])
                qtd += 1


def average_prices(first, last, table, message='Not found.'):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from %s where prod_price >= ? and prod_price <= ?' % table, (first, last))
            qtd = 0
            rows = []
            while True:
                register = cursor.fetchone()
                if register is None:
                    if qtd == 0:
                        print(message)
                    break
                print('Product: %s Price: %.2f' % register[1:])


def update(table, value1, value2, field1, field2, message='Update successfully.'):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('update {0} set {1} = ? where {2} = ?'
                           .format(table, field1, field2), (value1, value2))
            record = cursor.rowcount
            if record == 1:
                print(message + ' %d altered.' % record)
            else:
                print('Aborted changes.')
                conn.rollback()


increase = lambda x, p: x + (x * (p/100))


def update_price_by_name(name, value, table, message='Update successfully.'):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('update {0} set prod_price = ? where prod_name = ?'
                           .format(table), (value, name))
            if cursor.rowcount == 1:
                print(message)
            else:
                print('Aborted changes')
                conn.rollback()


def update_price(perc, table, message='Modifications made successfully.'):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from {0}'.format(table))
            registers = cursor.fetchall()
            qtd = 0
            for register in registers:
                cursor.execute('update {0} set prod_price = ? where prod_name = ?'
                               .format(table), (increase(register[2], perc), register[1]))
                qtd += 1
            print(message + ' Updates: ', qtd)


def delete_product(table, name, message='Deleted successfully.'):
    with sqlite3.connect('Prices.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('delete from {0} where prod_name = ?'.format(table), (name,))
            if cursor.rowcount == 1:
                print(message)
            else:
                conn.rollback()
                print('Aborted changes.')


def main():
    PRODUTOS = [('Amaciante Omo', 5.99),
                ('Maca Prata', 0.30),
                ('Sorvete (KIBOM) 1L', 15.99),
                ('Banana maca', 0.30),
                ('Couve flor', 1.53),
                ('Arroz Tiurbano', 5.99),
                ('Creme de leite', 5.70),
                ('Bolacha vitarela', 5.70),
                ('Coca-Cola 2,5L', 7.70)]
'''
    create_table('prices')
    insert_products(PRODUTOS)
    consult_all_table('prices')
    search_price('Creme de leite', 'prices', 'Produto nao encontrado.')
    average_prices(5.70, 7.70, 'prices', 'Produto nao encontrado')
    update('prices', 'Coca-Cola 3,0L', 7.85, 'prod_name', 'prod_price')
    update_price(10, 'prices')
    update_price_by_name(input('Produto: '), float(input('Novo valor: ')), 'prices')
    delete_product('prices', 'Bolacha vitarela')
'''

main()
