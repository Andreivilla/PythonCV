import random
def sorteia():
    list = []
    for i in range(5):
        n = random.randint(1, 100)
        list.append(n)
    return(list)

def somapar(list):
    soma = 0
    for i in list:
        if i%2 == 0:
            soma += i
    return soma


list = sorteia()
print('Lista sorteada: {}'.format(list))
soma = somapar(list)
print('Soma de pares: {}'.format(soma))
