sexo = str(input('Digite seu sexo(M/F): ')).strip().upper()
while sexo not in "MF":
    sexo = str(input('sexo invalido, digite outro valor: '))
print('sexo = {}'.format(sexo))