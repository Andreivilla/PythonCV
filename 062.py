primeiro = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razao: '))
i = 10
j = 1
while i != 0: 
    while j <= i:
        print(primeiro)
        primeiro += razao
        j += 1
    j = 1
    i = int(input('Mostrar mais quantos numeros(digite 0 pra sair): '))
