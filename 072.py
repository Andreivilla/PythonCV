ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Qual numero vc deseja escrever: '))
    if 0 <= n <= 20:
        break
    else:
        print('-----Valor invalido-----')

print(ext[n])
