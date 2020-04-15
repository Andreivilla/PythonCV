ns = (int(input('n1: ')), 
int(input('n2: ')), 
int(input('n3: ')), 
int(input('n4: ')),)
n9s = 0
pares = 0
primeiro3 = 0
print('Numeros pares: ')
for i in range(4):
    if ns[i] == 9:
        n9s += 1
    if ns[i] % 2 == 0:
        print('{}'.format(ns[i]), end=' ')        
        pares += 1
if pares == 0:
    print('\nNão existem numeros pares')
print('\nNumeros 9: {}'.format(n9s))
while primeiro3 < 4:
    if ns[primeiro3] == 3:
        print('Primeiro 3 na posicao: {}'.format(primeiro3))
        break
    elif primeiro3 == 3: 
        print('Não existe valor 3')
    primeiro3 += 1