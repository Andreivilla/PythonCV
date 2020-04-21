jogador = {}
gols = []
npartidas = 0
total_gols = 0
jogador['Nome'] = str(input('Nome do jogador: '))
npartidas = int(input('Numero de partidas: '))

for i in range(0, npartidas, +1):
    g =  int(input('Partida {}: '.format(i)))
    total_gols += g
    gols.append(g)

jogador['Gols'] = gols[:]
gols.clear()
jogador['Total'] = total_gols

print(10*'=*=')
print('Nome: {}'.format(jogador['Nome']))
print(10*'=*=')
for i, j in enumerate(jogador['Gols']):
    print('    Partida {}: {}'.format(i, j))
print(10*'=*=')
print('Total de gols: {}'.format(jogador['Total']))