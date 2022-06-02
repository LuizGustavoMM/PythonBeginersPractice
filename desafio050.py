soma = 0
print('Digite 6 valores inteiros e saiba a soma dos pares: ' .format(end=' '))
for c in range(1, 7):
    val = int(input(''))
    if val % 2 == 0:
        soma += val
print('A soma dos valores é: {}'.format(soma))