frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('A')+1))
print('A ultima ocorencia de A apareceu na posição: {}'.format(frase.rfind('A')+1))