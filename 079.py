vet = []
while True:
    n = int(input('Digite um valor: '))
    if n not in vet:
        vet.append(n)
        print('Valor adicionado')
    else:
        print('Numero repetido não adicionar')
    op = str(input('vc deseja continuar?(S/N): '))
    if op in 'Nn':
        break 
for i in range(0, len(vet), +1):
    for j in range(i, len(vet), +1):
        if vet[i] > vet[j]:
            h = vet[i]
            vet[i] = vet[j]
            vet[j] = h
for i in range(len(vet)):
    print('{}'.format(vet[i]), end=' ')