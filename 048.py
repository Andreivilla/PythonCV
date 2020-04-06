soma = 0
nimpar = 0
for i in range(0, 501, +1):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        nimpar += 1
print('Soma: {}'.format(soma))
print('Numeros impares multiplos de 3: {}'.format(nimpar))