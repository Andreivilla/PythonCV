import random
computador = random.randint(0, 5)#gerar numero aleatorio para o pc e 0 a 5
print('-:-'*10)
print('adivinhe um numero de 0 a 5: ')
print('-:-'*10)
jogador = int(input())
if jogador == computador:
    print('Acertou')
else:
    print('Errou, o correto era {}'.format(computador))