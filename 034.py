salario = float(input('Digite se salario: '))
if salario >= 1250:
    print('Seu salario agr vale: {}'.format(salario*1.1))
else:
    print('Seu salario agr vale: {}'.format(salario*1.15))