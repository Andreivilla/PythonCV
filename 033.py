n1 = int(input())
n2 = int(input())
n3 = int(input())
#definir maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
#definir menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3

print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))