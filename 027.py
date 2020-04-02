n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Primeiro nome é:  {}'.format(nome[0]))
print('ultimo nome é: {}'.format(nome[len(nome)-1]))