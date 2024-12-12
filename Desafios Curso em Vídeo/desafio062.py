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
maistermos = int(input('\nCaso deseja saber mais termos digite 1, caso queira continuar digite 0!\n\nR: '))
decisao = 0
while decisao == 0:
    if maistermos == 1:
        cont = 0
        while cont != 9:
            soma = soma + r
            cont += 1
            print('{}'.format(soma), end='-> ')
        escolha = 0
        escolha = int(input('\nCaso deseja saber mais termos digite 1, caso queira continuar digite 0!\n\nR: '))
        if escolha == 1:
            decisao == 0
        else:
            decisao += 1
    else:
        cont == 9
print('ACABOU!')