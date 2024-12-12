import random

par = []
impar = []

for i in range(20):
    num = random.randint(1, 100)
    if num % 2 == 1:
        impar.append(num)
    if num % 2 == 0:
        par.append(num)

print('Números pares: ', par)
print('Números impares: ', impar)