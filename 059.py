while True:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    op = int(input('''
1- somar
2- multiplicar
3- maior
4- digitar novos numeros
5- sair do programa
Escolha uma operação: 
'''))
    if op == 1:
        print('{}'.format(n1+n2))
    elif op == 2:
        print('{}'.format(n1*n2))
    elif op == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif op == 4:
        print('Digite novos valores')
        continue
    elif op == 5:
        break
    else:
        print('Opção invalida')