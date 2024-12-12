import math
n = float(input('Saiba o seno, cosseno e tangente de um ângulo desejado: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O seno do ãngulo {} é {:.2f}. \nO cosseno do ângulo {} é {:.2f}. \nA tangente do ângulo {} é {:.2f}.' .format(n, s, n, c,n , t))
