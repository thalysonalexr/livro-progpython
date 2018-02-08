salario = float(input("Salario? "))
porcent = float(input("Aumento? "))

aumento = salario * (porcent/100)
salario = salario + aumento

print("Novo salario: %.2f R$" %(salario))
print("Obteve um aumento de %.2f R$" %(aumento))
