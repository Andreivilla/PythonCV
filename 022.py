nome = str(input('digite seu nome completo: '))
print('Maisculas: {}'.format(nome.upper()))
print('Minusculas: {}'.format(nome.lower()))
print('Numero de letras: {}'.format(len(nome)-nome.count(' ')))