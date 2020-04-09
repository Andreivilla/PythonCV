total_gasto = custo_100 = c = 0
while True:
    produto = str(input('Nome do produto: ')).upper()
    preco = int(input('Preço do produto: '))
    total_gasto += preco
    if c == 0:
        menor_preco = preco
    if preco <= menor_preco:
        menor_preco = preco
        nome_menor_preco = produto
    if preco >= 100:
        custo_100 += 1
    c += 1
    op = str(input('Cadrastar mais um produto(S/N): ')).upper()
    if op == 'N':
        break
print('Total gasto: {}'.format(total_gasto))
print('Total de produtos: {}'.format(c))
print('Produtos mais caros que 100: {}'.format(custo_100))
print('Nome do produto mais barato: {}'.format(nome_menor_preco))