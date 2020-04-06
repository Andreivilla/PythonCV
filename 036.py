valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o valor do salario: '))
anos = float(input('Em quantos anos ira pagar: '))
prestacao = valor_casa/(anos*12)
print('Valor da prestação: {}'.format(prestacao))
if ((salario*0.3) < prestacao):
    print('Emprestimo concedido')
else:
    print('Emprestimo não pode ser concedido')