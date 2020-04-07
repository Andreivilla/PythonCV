import datetime 
atual = datetime.date.today().year
maiores = 0
menores = 0
for i in range(1, 8, +1):
    nasc = int(input('Ano de nascimento da {} pessoa: '.format(i)))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Maiores de idade: {}'.format(maiores))
print('Menores de idade: {}'.format(menores))