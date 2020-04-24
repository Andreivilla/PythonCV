def leiaSN(msg):#verificar se a resposta é sim ou não
    while True:
        escolha = str(input(msg))
        if escolha in 'SsNn':
            if escolha in 'Ss':
                return escolha
                break
            else:
                return escolha
                break
        else:
            print('Resposta invalida')

def notas():
    count_notas = 0#contador de notas
    lista_notas = []#lista para armaxenar todas as notas
    soma_notas = 0#variavel para armazenar o somatorio de notas
    dic = {} #dicionario de retorno
    while True:#dar entrada nas notas
        nota = float(input('Digite a nota: '))
        lista_notas.append(nota)#adiciona nota alista
        soma_notas += nota
        count_notas += 1
        op = leiaSN('Voce deseja digitar mais uma nota (S/N)?')#verifica se deve seguir o loop
        if op in 'Nn':
            break
    
    for i in range(0, len(lista_notas)):#loop para verificar maior e menor nota
        if i == 0:
            maior_nota = menor_nota = lista_notas[i]
        if maior_nota > lista_notas[i]:
            maior_nota = lista_notas[i]
        elif menor_nota < lista_notas[i]:
            menor_nota = lista_notas[i]

    media_turma = soma_notas/count_notas#calcula media

    #adicionar ao dicionario
    dic['Nnotas'] = count_notas
    dic['Maior nota'] = maior_nota
    dic['Menor nota'] = menor_nota
    dic['Media'] = media_turma
    return dic#retorna dicionario a funcao principal

dic = {}
dic = notas()
for i, j in dic.items():
    print(i,j)