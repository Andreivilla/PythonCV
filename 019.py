import random
aluno1 = str(input('Aluno1: '))
aluno2 = str(input('Aluno2: '))
aluno3 = str(input('Aluno3: '))
aluno4 = str(input('Aluno4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('o escolido é {}'.format(random.choice(lista)))