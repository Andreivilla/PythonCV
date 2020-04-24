def leiaInt():
    while True:
        n = str(input('Digite um valor inteiro: '))
        if n.isnumeric():
            valor = int(n)
            return valor
            break
        else:
            print('Valor invalido')


num = (leiaInt())
print(num)