vet = []
for i in range(0, 5, +1):
    vet.append(float(input('N[{}]: '.format(i+1))))
maior = menor = vet[0]
for i in range(0, 5, +1):
    if menor < vet[i]:
        menor = vet[i]
    if maior > vet[i]:
        maior = vet[i]
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))