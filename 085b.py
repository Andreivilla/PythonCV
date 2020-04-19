vet = [[], []]
for i in  range(7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        vet[0].append(n)
    else:
        vet[1].append(n)

vet[0].sort()
vet[1].sort()

print('Pares: {}'.format(vet[0]))
print('Impares: {}'.format(vet[1]))