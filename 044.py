preco = float(input('Preco do produto: '))
pagamento = int(input('''Selecione um modo de pagamento:
1- A vista dinheiro/cheque (10% de desconto) 
2- A vista  no cartão (5% de desconto)
3- 2x no cartão
4- 3x ou mais no cartão (20% de juros)
'''))
if pagamento == 1:
    print('Valor a pagar: {}'.format(preco*0.9))
elif pagamento == 2:
    print('Valor a pagar: {}'.format(preco*0.95))
elif pagamento == 3:
    print('Valor a pagar: {}'.format(preco))
elif pagamento == 4:
    print('Valor a pagar: {}'.format(preco*1.2))

