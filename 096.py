def area(larg=0, comp=0):
    return larg*comp


print('Defina as medidas do terreno')
l = float(input('Largura: '))
c = float(input('Cumprimento: '))
print('Area: {}'.format(area(l, c)))
