print('Digite três números e saiba qual o maior entre eles!')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 and n1 > n3:
    print('O número {}, é o maior.'.format(n1))
elif n2 > n3 and n2 > n1:
    print('O número {}, é o maior.' .format(n2))
elif n3 > n1 and n3 > n2:
    print('O número {}, é o maior.' .format(n3))
if n3 < n1 and n3 < n2:
    print('O número {}, é o menor.' .format(n3))
elif n2 < n1 and n2 < n3:
    print('O número {}, é o menor.' .format(n2))
elif n1 < n3 and n1 < n2:
    print('O número {}, é o menor.' .format(n1))
