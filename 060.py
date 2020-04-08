while True:
    n = int(input('Digite um valor(digite 0 para sair): '))
    if n == 0:
        break
    elif n < 0:
        print('Resposta invalida')
        continue
    else:
        fat = 1
        while n > 0:
            fat = fat*n
            n -= 1
        print('Fatorial: {}'.format(fat))