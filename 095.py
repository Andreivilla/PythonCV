jogador = {}
gols = []
lista_jogadores = []
npartidas = 0
total_gols = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    npartidas = int(input('Numero de partidas: '))

    for i in range(0, npartidas, +1):
        g =  int(input('Partida {}: '.format(i)))
        total_gols += g
        gols.append(g)

    jogador['Gols'] = gols[:]#adicionar lista de gols aop dicionario gols
    gols.clear()
    jogador['Total'] = total_gols#adicionar soma de gols a total

    lista_jogadores.append(jogador.copy())#adicionar jogaddoir alista de jogadores
    jogador.clear()#limpando dicionario para o proximo jogador
    total_gols = 0#zerar do contador de jogos

    op = str(input('Deseja adicionar mais pessoas(S/N): '))#verificar repeticao
    if op in 'Nn':
        break

print(10*'=*=')
print('Cod.    Nome    gols    total')#printar resultados
for i, j in enumerate(lista_jogadores):
    print('{}   {}   {}   {}'.format(i, j['Nome'], j['Gols'], j['Total']))

print(10*'=*=')
while True:
    op = int(input('Mostrar dados de um jogador(negativo para parar): '))
    if op < 0:
        break
    print('Nome do jogador: {}'.format(lista_jogadores[op]['Nome']))
    for i, j in enumerate(lista_jogadores[op]['Gols']):
        print('Partida {}: {}'.format(i, j))
    print(10*'=*=')



