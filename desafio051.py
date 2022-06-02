t = int(input('Digite o primeiro termo de uma P.A. para saber os outro 9 termos: '))
r = int(input('Agora digite a razão entre os termos: '))
soma = 0
soma = soma + t
print(t, end='-> ')
for c in range(1 ,10):
    soma = soma + r
    print('{}' .format(soma), end='-> ')
print('ACABOU!')