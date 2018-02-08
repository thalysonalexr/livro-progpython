import sqlite3

feriados = [["2014-01-01", "Confraternização Universal"], ["2014-04-21", "Tiradentes"], ["2014-05-01", "Dia do trabalhador"], ["2014-09-07", "Independência"], ["2014-10-12", "Padroeira do Brasil"], ["2014-11-02", "Finados"], ["2014-11-15", "Proclamação da República"], ["2014-12-25", "Natal"] ]
with sqlite3.connect("brasil.db") as conexão:
    conexão.execute("create table feriados(id integer primary key autoincrement, data date, descrição text)")
    conexão.executemany("insert into feriados(data,descrição) values (?,?)", feriados)