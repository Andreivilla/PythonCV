import random
vitorias = 0
while True:
    computador = random.randint(1,10)
    palpite = str(input('Par ou Impar(I/P): ')).upper()
    jogaddor = int(input('Digite um valor: '))
    soma = computador + jogaddor
    if soma % 2 == 0:
        PI = 'P'
    else:
        PI = 'I'
    if PI == palpite:
        print('VC ganhou')
        vitorias += 1
    else: 
        break
print('Vitorias: {}'.format(vitorias))