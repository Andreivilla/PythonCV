import datetime
dic = {}
dic['Nome'] = str(input('Nome: '))
dic['Ano de nascimento'] = int(input('Ano de nascimento: '))
dic['Idade'] = datetime.datetime.now().year - dic['Ano de nascimento']
dic['Carteira de trabalho'] = int(input('Carteira de trabalho(0 para não possui): '))

if dic['Carteira de trabalho'] == 0:
    dic['Carteira de trabalho'] = 'não possui'
else:
    dic['Ano de contratacao'] = int(input('Ano de contratacao: '))
    dic['Salario'] = float(input('Salario: '))
    dic['Aposentadoria'] = dic['Idade'] + ((dic['Ano de contratacao'] + 35) - datetime.datetime.now().year)

print(30*'=*=')

for i, j in dic.items():
    print('{}: {}'.format(i, j))