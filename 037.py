n = int(input('Digite um numero: '))
opcao = int(input('''escolha uma base para conversão:
1 - Binario
2 - Octal
3 - Hexadecimal 
'''))
if(opcao == 1):
    print('{}'.format(bin(n)))
elif(opcao == 2):
    printf('{}'.format(oct(n)))
elif(opcao == 3):
    print('{}'.format(hex(n)))
else:
    print('Opcao invalida')