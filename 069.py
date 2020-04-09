homens = 0
mulheres_20 = 0
maiores_18 = 0
while True:
    sexo = str(input('Sexo(M/F): ')).upper()
    idade = int(input('Idade: '))
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    if idade >= 18:
        maiores_18 += 1
    op = str(input('Cadrastar mais uma pessoa(S/N): ')).upper()
    if op == 'N':
        break
print('Maiores de 18: {}'.format(maiores_18))
print('Homens: {}'.format(homens))
print('Mulheres com menos de 20: {}'.format(mulheres_20))