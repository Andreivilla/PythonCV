import random
import time
import operator
dados = {'Jogador 1': random.randint(1,6),
'Jogador 2': random.randint(1,6),
'Jogador 3': random.randint(1,6),
'Jogador 4': random.randint(1,6),
}
ranking = []
print('--- Valores sorteados ---')
for i, j in dados.items():
    print('{}: {}'.format(i, j))
    time.sleep(1)

ranking = sorted(dados.items(), key=operator.itemgetter(1), reverse=True)
#sorted ordena vetor/ key especifica qual posicao ordenar/ reverse inverte para orden decrescente
print('----- Podio -----')
for i in range(0, len(ranking)):
    print('{}: {}'.format(ranking[i][0], ranking[i][1]))
    time.sleep(1)