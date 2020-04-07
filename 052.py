n = int(input('Digite um valor: '))
div = 0
for i in range(1, n, +1):
    if n % i == 0:
        div += 1
if div > 2:
    print('Não é primo')
else:
    print('É primo')