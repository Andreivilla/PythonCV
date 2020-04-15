valor = int(input('digite o valor a ser sacado: '))
const50 = const20 = const10 = const1 = 0
while True:
    if valor / 50 > 0:
        const50 = valor // 50
        valor -= (50*const50)
    if valor / 20 > 0:
        const20 = valor // 20 
        valor -= (20*const20)
    if valor / 10 > 0:
        const10 = valor // 10 
        valor -= (10*const10)
    if valor / 1 > 0:
        const1 = valor // 1
        valor -= (1*const1)    
    break
print('notas de 50: {}'.format(const50))
print('notas de 20: {}'.format(const20))
print('notas de 10: {}'.format(const10))
print('notas de 1: {}'.format(const1))