import random
n = (random.randint(1,10), random.randint(1,10), random.randint(1,10), 
random.randint(1,10), random.randint(1,10))
menor = n[1]
maior = n[1]
for i in range(5):
    print('{}'.format(n[i]), end=' ')
    print('')
    if n[i] > maior:
        maior = n[i]
    if n[i] < menor:
        menor = n[i]
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))