import moeda

n = int(input('Digite um valor: '))
a = int(input('Digite um aumento: '))
d = int(input('Digite um valor para dimuir: '))


print(moeda.aumentar(n, a))
print(moeda.diminuir(n, d))
print(moeda.dobrar(n))
print(moeda.metade(n))