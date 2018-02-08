import sqlite3

conexão = sqlite3.connect("brasil.db")
conexão.row_factory = sqlite3.Row
print("%3s %-20s %12s" % ("Id","Estado","População"))
print("="*37)
for estado in conexão.execute("select * from estados order by Id desc"):
    print("%3d %-20s %12d" %
          (estado["id"],
           estado["nome"],
           estado["população"]))
conexão.close()

'''
SQL ORDENAÇÃO

select * from TABELA order by CAMPO  /// Crescente
select * from TABELA order by CAMPO desc

'''