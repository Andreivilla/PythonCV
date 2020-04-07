for i in range(5):
    peso = float(input('Digite o peso: '))
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))