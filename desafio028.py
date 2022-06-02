import random
print('-=-' * 20)
print('Jogo da Advinhação!')
num1 = int(input('Digite um número de 0 a 5 e saiba se você acertou! '))
num = random.randint(0, 5)
if num1 == num:
    print('Parabens você acertou, o número era {}!'.format(num1))
else:
    print('Você errou! O número era {}!'.format(num))
print('-=-' * 20)