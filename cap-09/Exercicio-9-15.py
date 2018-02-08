from random import randint


def carregar_palavras():
    lista = []
    arquivo = open('palavras_secretas.txt', encoding='utf-8')
    for linha in arquivo.readlines():
        lista.append(linha.strip())
    arquivo.close()
    return lista


def exibir_recordes(mensagem='-- Melhores jogadores --'):
    jogadores = carregar_placar()
    if not jogadores:
        return
    print(mensagem)
    print('nº| Nome:'+' ' * 17 + ' Pontos:')
    lista = list(jogadores.items())
    lista.sort(key=lambda score: score[1])
    lista.reverse()
    for i, e in enumerate(lista):
        print('{0} | {1:-<25} {2}'.format(i+1, e[0], e[1]))
        if i == 4:
            break


def gravar_jogador(nome, nome_arquivo='jogadores.txt',pontos=1):
    jogadores = carregar_placar()
    arquivo = open(nome_arquivo, 'a')
    if nome not in jogadores:
        arquivo.write(nome + ';' + str(pontos) + '\n')
    else:
        atualizar_pontuacao(nome)
    arquivo.close()


def carregar_placar(nome_arquivo='jogadores.txt', simbolo=';'):
    dic = {}
    arquivo = open(nome_arquivo, encoding='utf-8')
    for linha in arquivo.readlines():
        aux = linha.split(';')
        dic[aux[0]] = int(aux[1])
    return dic


def atualizar_pontuacao(nome, nome_arquivo='jogadores.txt'):
    jogadores = carregar_placar()
    if nome in jogadores:
        jogadores[nome] += 1
    arquivo = open(nome_arquivo, 'w', encoding='utf-8')
    for chave in jogadores:
        arquivo.write(chave + ';' + str(jogadores[chave]) + '\n')
    arquivo.close()


digitadas = []
acertos = []
erros = 0
lista = carregar_palavras()
palavra = lista[randint(0, len(lista)-1)]


while True:
    exibir_recordes()
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        gravar_jogador(input('Digite seu nome: '))
        break
    while True:
        tentativa = input("\nDigite uma letra:").lower().strip()
        if len(tentativa) > 1:
            print('Apenas uma letra!')
        else:
            break
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print("'{0}' era a palavra secreta!".format(palavra))
        break