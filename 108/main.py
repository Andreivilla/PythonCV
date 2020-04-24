import moeda

n = int(input('Digite um valor: '))
print('Dobro: {}'.format(moeda.dobrar(n)))
print('Metade: {}'.format(moeda.metade(n)))
print('Aumento 10: {}'.format(moeda.aumentar(n, 10)))
print('Diminuir 10: {}'.format(moeda.diminuir(n, 10)))