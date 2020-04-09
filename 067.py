n = 0
while n >= 0:
    n = int(input('Digite um valor(digite um valor negativo para parar): '))
    if n < 0:
        break
    for i in range(1, 11, +1):
        print('{} x {} = {}'.format(n,i,(n*i)))