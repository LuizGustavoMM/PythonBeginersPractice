print('Digite valores e saiba se é possivel formar um triângulo.')
l1 = float(input('Lado 1: '))
l2 = float(input('lado 2: '))
l3 = float((input('Base: ')))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos citados podem formar um triângulo e será ', end='')
    if l1 == l2 == l3:
        print('equilátero.')
    elif l1 != l2 != l3 != l1:
        print('escaleno.')
    else:
        print('isóceles.')
else:
    print('Não é possível.')