somaidade = 0
maioridadehomem = 0
nomevelho = 0
mulheresm = 0
for p in range(1, 5):
    print('------ {}° Pessoa ------' .format(p))
    nome = str(input('Nome: ')).strip()
    idade =  int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        mulheresm += 1
print('A Média da idade do grupo é de {} anos.' .format(somaidade/4))
print('O homem mais velho tem {} anos e seu nome é {}.' .format(maioridadehomem, nomevelho))
print('Tem {} mulheres menores de 20 anos.' .format(mulheresm))