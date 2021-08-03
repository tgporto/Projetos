import random

pratos = ['massa', 'sopa de feijão', 'soja grossa', 'soja fina', 'hamburger', 'arroz com alho', 'omelete', 'jardineira']
molhos = ['molho branco', 'soja fina', 'molho vermelho']
sucos = ['cajú', 'goiaba', 'limão', 'uva']

def comida():
    x = input('O que vamos comer hoje?\nPratos(1) Molhos(2) Sucos(3)\n')

    if (x == '1'):
        print('Que tal preparar ', random.choice(pratos),'?')
    elif (x == '2'):
        print('Para acompanhar, que tal ', random.choice(molhos),'?')
    elif (x == "3"):
        print('Que tal beber um suco de', random.choice(sucos),'?')
    else:
        print('opção inválida, escolha novamente')
        return comida()
    volta()


def volta():
    z = input('Deseja escolher novamente? (s/n)')

    if (z == 's'):
        return comida()
    elif (z == 'n'):
        print('Bom apetite!')
    else:
        print('opção inválida, escolha novamente')
        return z

comida()
