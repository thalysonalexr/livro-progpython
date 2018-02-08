def pesquisa(lista, valor):
    if valor in lista:
        return lista.index(valor)
    else:
        return None


print(pesquisa([1,2,3,4,5,6], 9))