palavras = ('aprender','programar', 'linguagem', 'python', 
'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 
'mercado', 'programador', 'futuro')
for i in range(len(palavras)):
    print('{}: '.format(palavras[i]), end=' ')
    for j in range(len(palavras[i])):
        if palavras[j] in 'aeiou':
            print(i, end=' ')
    print('')