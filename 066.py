cont = 0
soma = 0
n = 0
op = 'S'
while op == 'S':
    cont += 1
    soma += n
    n = int(input('Digite um numero: '))
    op = str(input('Voce quer digitar mais um valor(S/N):')).upper()
print('Soma: {}'.format(soma))
print('Numero de numeros: {}'.format(cont))