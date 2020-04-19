aluno = []
soma_alunos = []
while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    for i in range(2):
        nota = float(input('Nota {}: '.format(i + 1)))
        aluno.append(nota)
    soma_alunos.append(aluno[:])
    aluno.clear()
    op = str(input('Adicionar mais um aluno(S/N): '))
    if op in 'Nn':
        break

print('No. NOME     MEDIA')
print('------------------')
for i in range(len(soma_alunos)):
    media = (soma_alunos[i][1] + soma_alunos[i][2]) / 2
    print('{}    {}    {}'.format(i, soma_alunos[i][0], media))

n = 0 
while n >= 0:
    n = int(input('Digite o indice do aluno prar ver notas(-1 para parar): '))
    if n < 0:
        break
    for i in range(1,3):
        print('Nota {}: {}'.format(i, soma_alunos[n][i]))