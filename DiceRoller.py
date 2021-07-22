from random import randint

dice1 = randint(1, 20)
dice2 = randint(1, 20)

print("Programa para rolagem de d20. Se não há vantagem/desvantagem, considere apenas o primeiro resultado")
print(dice1, dice2)


if (dice1 == 1) or (dice2 == 1):
    print("Ops! Falha crítica!")

elif (dice1 == 20) or (dice2 == 20):
    print("Acerto crítico!")