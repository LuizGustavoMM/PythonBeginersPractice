import math
print('Digite os catetos de um triangulo retângulo para saber sua hipotenusa!')
ca = float(input('Digite o CatetoA: '))
cb = float(input('Digite o CatetoB: '))
hip = math.hypot(ca, cb)
print('O valor da Hipotenusa de um triângulo retângulo de lados {} e {} é equivalente a: {:.1f}'.format(ca, cb, hip))
