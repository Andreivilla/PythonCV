mat = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = int(input('Mat[{}][{}]: '.format(i,j)))

for i in range(0,3):
    for j in range(0,3):
        print(mat[i][j],end=' ')
    print('')