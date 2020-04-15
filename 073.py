times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 
'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 
'Fortaleza','Goiás' ,'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 
'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('Cinco primeiros colocados: ')
for i in range(5):
    print('{}o - {}'.format((i+1), times[i]))

print('\n4 Ultimos: ')
for i in range(16, 20, +1):
    print('{}o - {}'.format((i+1), times[i]))

for i in range(20):
    if times[i] == 'Chapecoense':
         print('\nChapecoense esta em {}'.format(i+1))