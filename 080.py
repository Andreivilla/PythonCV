vet = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > vet[-1]: 
        vet.append(n)
    else:
        j = 0
        while j < len(vet):
            if n <= vet[j]:
                vet.insert(j, n)
                break
            j+=1
for i in range(0, len(vet)):
    print('{}'.format(vet[i]), end=' ')