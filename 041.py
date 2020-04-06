import datetime
atual = datetime.date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFALTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')