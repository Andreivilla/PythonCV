count_pessoas = 0
disc_pessoas = {}
list_pessoas = []
while True:
    disc_pessoas['Nome'] = str(input('Nome: '))
    disc_pessoas['Sexo'] = str(input('Sexo(M/F): ')).upper()
    disc_pessoas['Idade'] = int(input('Idade: '))
    list_pessoas.append(disc_pessoas.copy())#copy para adicionar dicionario a lista
    disc_pessoas.clear()#liberar dicionario
    count_pessoas += 1
    
    op = str(input('Deseja adicionar mais pessoas(S/N): '))#verificar repeticao
    if op in 'Nn':
        break

soma_idade = 0 #somar idades
for i in list_pessoas:
    soma_idade += i['Idade']
idade_media = soma_idade/count_pessoas

#criar lista de mulheres
lista_mulheres = []
for i in list_pessoas:
    if i['Sexo'] == 'F':
        lista_mulheres.append(i)

#criar lista de ideades acima da media
lista_acima_media = []
for i in list_pessoas:
    if i['Idade'] > idade_media:
        lista_acima_media.append(i)

print('Numero de pessoas cadastradas: {}'.format(count_pessoas))
print('Mulheres: \n')
for i in lista_mulheres:
    print(i)
print('Acima da media: \n')
for i in lista_acima_media:
    print(i)