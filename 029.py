velocidade = float(input('Velocidade do caro: '))
if velocidade > 80:
    print('Vc foi multado, no valor de: {:.2f}'.format((velocidade - 80)*7))