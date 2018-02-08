filmes = {
     "drama": ["Cidadão Kane","O Poderoso Chefão"],
     "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
     "policial": ["Chuva Negra","Desejo de Matar","Difícil de Matar"],
     "guerra": ["Rambo","Platoon","Tora!Tora!Tora!"]}

pagina = open("filmes.html","w", encoding = "utf-8")

pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
     pagina.write("<h1>%s</h1>" % c)
     for e in v:
         pagina.write("<p>%s</p>" % e)
pagina.write("""
</body>
</html>
""")
pagina.close()