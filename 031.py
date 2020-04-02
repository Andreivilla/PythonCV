dist = float(input('Digite a distancia da viagem: '))
if dist <= 200:
    print('o valor da viagem é: {}'.format(dist*0.5))
else:
    print('o valor da viagem é: {}'.format(dist*0.45))