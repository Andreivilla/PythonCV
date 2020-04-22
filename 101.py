import datetime
def voto(ano):
    atual = datetime.date.today().year
    idade = atual - ano
    if idade < 16:
        return 'Negado'
    elif idade >= 16 and idade < 18:
        return 'Opcional'
    else:
        return 'Obrigatorio'

n = int(input('Digite o seu ano de nascimento: '))
print('Sua condição de voto é : {}'.format(voto(n)))