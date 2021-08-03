from random import randint

print("Programa para rolagem de d20.")

def roller():
    x = input("Você está rolando com vantagem/desvantagem? (s/n)")

    dice1 = randint(1, 20)
    dice2 = randint(1, 20)

    if x == "s":
        print(dice1, dice2)
        if (dice1 == 1) or (dice2 == 1):
            print("Ops! Falha crítica!")
        
        elif (dice1 == 20) or (dice2 == 20):
            print("Acerto crítico!")

    elif x == "n":
        print(dice1)
        if (dice1 == 1):
            print("Ops! Falha crítica!")
        
        elif (dice1 == 20):
            print("Acerto crítico!")
    
    return fechar()
   
            

def fechar():
    y = input("Deseja rolar novamente? (s/n)")

    if y == "s":
        return roller()

    elif y == "n":
        print("Boa sorte!")
        

roller()