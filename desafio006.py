print('Este script mostrará o dobro, triplo e a raiz quadrada de número inteiro de sua escolha.')
n = int(input('Digite o número de sua escolha: '))
d = n*2
t = n*3
r = n**(1/2)
print(' O dobro do seu número é {}.\n O triplo do seu número é {}. \n A raiz quadrado do seu número é {:.3f}.'.format(d, t, r))
