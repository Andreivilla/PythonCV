n1 = float(input('digite o  valor do lado 1: '))
n2 = float(input('digite o  valor do lado 2: '))
n3 = float(input('digite o  valor do lado 3: '))
if n1+n2 > n3 and n2+n3 > n1 and n1+n3 > n2:
    print('forma triangulo')
else:
    print('Não forma triangulo')