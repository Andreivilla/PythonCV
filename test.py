def leiaInt():
    while True:
        n = str(input('Digite um valor inteioro: '))
        if n.isdigit():
            valor = float(n)
            return valor
            break
        else:
            print('Valor invalido')


num = (leiaInt())
print(num)