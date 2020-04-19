vetpar = []
vetimpar = []
imparpar = []
for i in range(7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        vetpar.append(n)
    else:
        vetimpar.append(n)

for i in range(0, len(vetpar), +1):
    for j in range(i, len(vetpar), +1):
        if vetpar[i] > vetpar[j]:
            h = vetpar[i]
            vetpar[i] = vetpar[j]
            vetpar[j] = h

for i in range(0, len(vetimpar), +1):
    for j in range(i, len(vetimpar), +1):
        if vetimpar[i] > vetimpar[j]:
            h = vetimpar[i]
            vetimpar[i] = vetimpar[j]
            vetimpar[j] = h

imparpar.append(vetimpar[:])
imparpar.append(vetpar[:])
vetimpar.clear()
vetpar.clear()

print(imparpar)
