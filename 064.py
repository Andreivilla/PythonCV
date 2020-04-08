cont = 0
soma = 0
n = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero(digite 999 para parar): '))

print('Soma: {}'.format(soma))
print('Numero de numeros: {}'.format(cont))