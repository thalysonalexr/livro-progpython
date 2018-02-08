import sys

tamanho = len(sys.argv)

if tamanho == 1:
    print(sys.argv[0])
else:
    try:
        nome = sys.argv[1]
        inicio = int(sys.argv[2])
        fim = int(sys.argv[3])
    except:
        print("Insira os parametros corretamente: [arquivo] [linha(i)][linha(f)]")
    else:
        arquivo = open(nome, "r")
        t = len(arquivo.readlines())
        arquivo.close()

        if inicio < 1:
            print("Linha de inicio minimo 1 maximo ", t)
        elif fim > t:
            print("Linha de fim maximo %d minimo 1" %(t))
        else:
            arquivo = open(nome, "r")
            for i, e in enumerate(arquivo.readlines()):
                if i >= (inicio-1) and i < fim:
                    print(e)
            arquivo.close()