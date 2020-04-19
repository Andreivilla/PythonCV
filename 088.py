import random
jogo1 = []
soma_jogos = []
ns = 0

palpites = int(input('Quantos palpites mostrar?: '))

for i in range(palpites):
    while ns < 6:
        n = random.randint(1,60)#gera numeros randomicos de 1 a 60
        if n not in jogo1:#se n não existir no vetor jogo
            jogo1.append(n)#armazenar ele
            ns += 1#contar numero armazenado
        else:
            continue
    soma_jogos.append(jogo1[:])#add ao vetor de jogos
    jogo1.clear()#limpar vetor jogo
    ns = 0

print('Palpites: ')
for i in soma_jogos:
    print(i)