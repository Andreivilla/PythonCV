vet = []
vetpar = []
vetimpar = []
while True:
    vet.append(int(input('Digite um valor: ')))
    op = str(input('Voce deseja continuar(N/S)? '))
    if op in 'Nn':
        break

for i in vet:
    if i % 2 == 0:
        vetpar.append(i)
    else:
        vetimpar.append(i)

print('Vetor: ')
for i in vet:
    print(i, end=' ')
print('\nPares do vetor: ')
for i in vetpar:
    print(i, end=' ')
print('\nImpares do vetor: ')
for i in vetimpar:
    print(i, end=' ')
