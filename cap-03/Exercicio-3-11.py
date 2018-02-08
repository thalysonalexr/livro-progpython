preco = float(input("Preco da mercadoria: "))
desco = float(input("Percentual de desconto: "))

valor = preco * (desco/100)
preco = preco - valor

print("Valor da mercadoria com o desconto de %d%% e de %.2f R$" %(desco, preco))
print("Valor do desconto e de %.2f R$" %(valor))
