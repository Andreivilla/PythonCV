lista = ('Lapis', 1.75, 
'Borracha', 2, 
'Caderno', 15.90, 
'Estojo', 25, 
'Transferidor', 4.2, 
'Compasso', 9.99, 
'Mochila', 120.32, 
'Canetas', 22.30,
'Livro', 34.9)

for i in range(0, len(lista), +2):
    print('{} ---------- {}'.format(lista[i], lista[i+1]))