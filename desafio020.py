import random
n1 = input('Digite o nome do primeiro aluno para que seja sorteada a ordem de apresentação: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
ns = [n1, n2, n3, n4]
random.shuffle(ns)
print('A ordem de apresentação será: {}'.format(ns))

