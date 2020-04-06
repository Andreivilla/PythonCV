import random
jogador = int(input('''Escolha uma jogada
1 - pedra
2 - Papel
3 - Tesoura
'''))
computador = random.randint(1,3)
if jogador == 1:
    if computador == 1:
        print('empate')
    elif computador == 2:
        print('Vc perdeu')
    elif computador == 3:
        print('Vc ganhou')
elif jogador == 2:
    if computador == 2:
        print('empate')
    elif computador == 3:
        print('Vc perdeu')
    elif computador == 1:
        print('Vc ganhou')
elif jogador == 3:
    if computador == 3:
        print('empate')
    elif computador == 1:
        print('Vc perdeu')
    elif computador == 2:
        print('Vc ganhou')
else:
    print('Escolha invalida')