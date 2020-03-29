import math
ca = float(input('Cateto Adjacente: '))
co = float(input('Cateto Oposto: '))
print('a hipotenusa vale: {:.2f}'.format(math.hypot(co,ca)))
#outra opção seria "from math import hypot"