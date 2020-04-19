mat = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = 0
soma_coluna3 = 0
maior_linha2 = 0
for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = int(input('Mat[{}][{}]: '.format(i,j)))

for i in range(0,3):
    for j in range(0,3):
        if mat[i][j] % 2 == 0:
            soma_par += mat[i][j]
        if j == 2:
            soma_coluna3 += mat[i][j]
        if i == 1:
            if mat[i][j] > maior_linha2:
                maior_linha2 = mat[i][j]

for i in range(0,3):
    for j in range(0,3):
        print(mat[i][j],end=' ')
    print('')

print('Soma dos valores pares: {}'.format(soma_par))
print('Soma dos elementos dacoluna 3: {}'.format(soma_coluna3))
print('Maior da linha 2: {}'.format(maior_linha2))