soma = c = 0
op = 'S'
while op == 'S':
    n = float(input('Digite um valor: '))
    soma += n
    c += 1
    op = str(input('Digitar novo valor(S/N): ')).upper()
print('Media: {}'.format((soma/c)))