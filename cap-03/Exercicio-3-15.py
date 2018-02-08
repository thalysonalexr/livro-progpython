quant_cigarros = int(input("Digite a quant. de cigarros fumados por dia: "))
anos = int(input("Quantos anos voce ja fumou: "))

total_minutos = quant_cigarros * 365 * anos
dias = total_minutos * 10
dias = dias / 60 # Achar horas
dias = dias / 24 # Achar dias

print("Vida restante %d dia(s)" %(dias))
