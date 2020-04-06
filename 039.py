import datetime
atual = datetime.date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
if(idade == 18):
    print('Deve se alistar esse ano')
elif(idade < 18):
    print('Faltam {} anos para o alistamento'.format(18 - idade))
else:
    print('Seu alistamento foi a {} anos'.format(idade - 18))