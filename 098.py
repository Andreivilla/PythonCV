def contador(a=0, b=0, c=0):
    i = a
    if c > 0:
        while i <= b:
            print(i)
            i += c
    elif c < 0:
        while i >= b:
            print(i)
            i += c
    else:
        print('Incremento invalido')


contador(1, 10, +1)
print('=*=')
contador(10, 0, -2)
print(10*'=*=')
comeco = int(input('Valor de inicio do contador: '))
fim = int(input('Valor do final do contador: ')) 
incremento = int(input('Incrememento: ')) 
contador(comeco, fim, incremento)