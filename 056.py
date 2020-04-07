soma_idade = 0
homem_velho = 0
mulheres_menos20 = 0
for i in range(1, 5, +1):
    print('Pessoa {}:'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    soma_idade += idade
    if sexo == 'F':
        if idade < 20:
            mulheres_menos20 += 1
    if sexo == 'M':
        if idade > homem_velho:
            homem_velho = idade
            nome_homem_velho = nome
print('Media de idade: {}'.format((soma_idade/4)))
print('Homem mais velho: {}'.format(nome_homem_velho))
print('Numero de mulheres com menos de 20 anos: {}'.format(mulheres_menos20))