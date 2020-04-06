a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
if  a+b > c and a+c > b and b+c > a:
    print('Forma triangulo: Sim')
    if a == b == c:
        print('Tipo do triangulo: Equilatero')
    elif a != b != c != a:
        print('Tipo do triangulo: Escaleno')
    else:
        print('Tipo do triangulo: Isosceles')
        
else:
    print('Forma triangulo: Não')