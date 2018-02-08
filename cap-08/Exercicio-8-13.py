import random

n = random.randint(1, 10)
chances = 3
while chances >= 1:
    x = int(input("Escolha um numero entre 1 e 10: "))
    if x == n:
        print("Voce acertou!")
        break
    else:
        print("Voce errou.")
    chances -= 1