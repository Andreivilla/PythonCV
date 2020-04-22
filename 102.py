def fat(n=0, show = False):
    fatorial = 1
    for c in range(n, 0, -1):
        fatorial *= c
    if show:
        print('{}'.format(fatorial))
    return fatorial

n = int(input('Numero para calculo fatorial: '))
print(fat(n, True))