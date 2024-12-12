from random import randint
numeros = []
multi1 = 1

for i in range(5):
    num = randint(1, 10)
    print(num)
    numeros.append(num)

for i in range(5):
    multi1 *= numeros[i]

print(f'A soma desses números é: {sum(numeros)}')
print(f'A multiplicação desses números é: {multi1}')
