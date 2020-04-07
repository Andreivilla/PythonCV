soma = 0
cont = 0
for i in range(6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Soma: {}'.format(soma))
print('Numero de Valores: {}'.format(cont))