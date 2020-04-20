aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'

for i, j in aluno.items():
    print('{}: {}'.format(i, j))