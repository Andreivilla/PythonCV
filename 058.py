import random
bot = random.randint(1,10)
jogador = 0
while jogador != bot:
    jogador = int(input('Dê um palpite de 1 a 10: '))
    if jogador < 1 or jogador > 10:
        print('Palpite invalido')
        continue
    if jogador == bot:
        break
    print('Errou')
print('Acertou')