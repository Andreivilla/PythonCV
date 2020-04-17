dados = []
list = []
pessoas = maior_peso = menor_peso =0 
while True:#ler dados
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu Peso: ')))
    list.append(dados[:])
    dados.clear()
    pessoas += 1 #conta pessoas
    op = str(input('Voce deseja continuar(N/S)? '))
    if op in 'Nn':
        break

#maior e menor peso
    for i in list:
        if i == 0:
            maior_peso = i[1]
            menor_peso = i[1]
        elif i[1] > maior_peso:
            maior_peso = i[1]
        elif i[1] < menor_peso:
            menor_peso = i[1]
        
print('Numero de pessoas: {}'.format(pessoas))
print('Maior peso: ')
for i in list:
    if i[1] == maior_peso:
        print('{}'.format(i[0]), end=' ')

print('\nMenor peso: ')
for i in list:
    if i[1] == menor_peso:
        print('{}'.format(i[0]), end=' ')