print('Digite valores e saiba se é possivel formar um triângulo.')
l1 = float(input('Lado 1: '))
l2 = float(input('lado 2: '))
base = float((input('Base: ')))
if ((l2-base)*-1) < l1 < l2 + base and ((l1-base)*-1) < l2 < l1+base and ((l1-base)*-1) < base < l1 + l2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível.')
