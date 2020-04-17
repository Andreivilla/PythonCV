exp = str(input('Digite a expressão: '))
abre = fecha = 0
for i in exp:
    if i == '(':
        abre += 1
    elif i == ')':
        fecha += 1
if abre == fecha:
    print('Numero correto de parenteses')
else:
    if abre > fecha:
        print('Faltam {}: )'.format((abre - fecha)))
    elif fecha > abre:
        print('Faltam {}: ('.format((fecha - abre)))