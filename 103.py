def ficha(nome, gols):
    dic = {}
    dic['Nome'] = nome
    dic['Gols'] = gols
    return dic


nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
ficha_jogador = {}
ficha_jogador = ficha(nome, gols)
print(10*'=*=')
print('Ficha do jogador: ')
for i, j in ficha_jogador.items():
    print('{}: {}'.format(i, j))