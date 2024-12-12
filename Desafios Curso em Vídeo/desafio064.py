num = -999
num1 = 0
qnt = -1
while num1 != 999:
    num1 = int(input('\nDigite os números que deseja saber a soma.\n[Digite "999" caso deseje parar]\n\nResposta: '))
    soma = num1 + num
    num = soma
    qnt += 1
print('\n\n\nA soma dos {} números foi {}.'.format(qnt, soma))