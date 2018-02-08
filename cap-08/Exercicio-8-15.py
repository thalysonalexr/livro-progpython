def imprime_lista(lista, nivel=1, i=0):
    for j, e in enumerate(lista):
        if type(e) == int:
            print("[" * nivel, e, "]")
        else:
            return imprime_lista(lista[j], nivel + 1, i + 1)
    if i == len(lista)-1:
        return


imprime_lista([1,[2,3,4,[5,6,7,[8,9,10,[11,12,13]]]]])