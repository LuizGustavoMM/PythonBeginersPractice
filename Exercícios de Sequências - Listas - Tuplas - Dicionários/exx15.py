a_cima_da_media = []
abaixo_da_media = []
notas = []
cont = 1
cont1 = 0

while True:
    nota = float(input(f'Digite a nota do {cont}° aluno: '))
    cont += 1
    if nota >= 1:
        notas.append(nota)
    else:
        break
print('\n')

for nota in notas:
    print(f'[{nota:.1f}]', end=' ')

print('\n')

for nota in notas:
    cont1 -= 1
    print(notas[cont1])

tamanho = len(notas)
media = sum(notas)/tamanho
print('\n')

print(f'Soma dos valores: {sum(notas)}')
print(f'Média das notas: {media}')

for nota in notas:
    if nota > media:
        a_cima_da_media.append(nota)
print('\n')
print(f'Valores a cima da média de: {media}')

for nota in a_cima_da_media:
    print(nota, end=' ')
print('\n')

for nota in notas:
    if nota < 7:
        abaixo_da_media.append(nota)

print(f'Valores abaixo de: 7')

for nota in abaixo_da_media:
    print(nota, end=' ')
print('\n')

print(30*'-', 'App média integra encerrado', 30*'-')