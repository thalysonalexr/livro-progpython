km = int(input("Digite em Km: "))
dias = int(input("Dias de aluguel: "))

preco = dias * 60
preco = preco + km * 0.15

print("O preco do aluguel ficou de %.2f R$" %(preco))
