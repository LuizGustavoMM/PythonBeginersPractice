t = int(input('Digite o primeiro termo de uma P.A. para saber os outro 9 termos: '))
r = int(input('Agora digite a razão entre os termos: '))
soma = 0
soma = soma + t
cont = 0
print(t, end='-> ')
while cont != 9:
    soma = soma + r
    cont += 1
    print('{}' .format(soma), end='-> ')
print('ACABOU!')