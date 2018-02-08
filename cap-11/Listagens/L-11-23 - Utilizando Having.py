import sqlite3

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
        select região, count(*) as total_estados, min(população),
               max(população), avg(população), sum(população) as tpop
        from estados
        group by região
        having total_estados > 5
        order by tpop desc"""):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))