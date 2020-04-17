vet = []
i = 0
while True:
    vet.append(int(input('Digite um valor(digite um numero negativo para parar): ')))
    if vet[i] < 0:
        break
    i += 1
print('Possui {} valores'.format(i))
for i in range(0, len(vet), +1):
    for j in range(i, len(vet), +1):
        if vet[i] > vet[j]:
            h = vet[i]
            vet[i] = vet[j]
            vet[j] = h
for i in vet:
    print(i, end=' ')
if 5 in vet:
    print('\npossui o valor 5')