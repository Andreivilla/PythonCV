def maior(n):
    maior = n[0]
    for i in n:
        if i > maior:
            maior = i
    print('Maior: {}'.format(maior))
num = [1,2,3,29,1,3]
maior(num)