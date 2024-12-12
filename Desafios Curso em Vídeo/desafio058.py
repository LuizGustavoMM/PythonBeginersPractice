from random import randint
print ('=-=' * 20)
print('Jogo da advinhação 2.0!')
num = randint(0, 10)
cont = 0
resposta = 11
while resposta != num:
    resposta = int(input('Tente advinhar o número de 0 a 10!\n\nresposta: '))
    cont += 1
print('\n\n\n\nO número era: {}\n\nVocê acertou em {} tentativas.' .format(num, cont))
print('\n\nFim!')