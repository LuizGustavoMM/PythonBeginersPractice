idades = [11, 13, 14, 10, 15, 16, 12, 17, 10, 14, 13, 11, 16, 17, 12, 15, 10, 12, 13, 14, 16, 17, 15, 11, 10, 14, 13, 12, 17, 15]
alturas = [1.39, 1.41, 1.46, 1.5, 1.55, 1.61, 1.66, 1.7, 1.42, 1.47, 1.49, 1.53, 1.59, 1.63, 1.68, 1.72, 1.4, 1.43, 1.48, 1.51, 1.56, 1.6, 1.65, 1.69, 1.44, 1.45, 1.52, 1.54, 1.58, 1.64]

media = sum(alturas)/30
cont = 0

for i in range(30):

    if idades[i] > 13 and alturas[i] < media:
        print(idades[i], end=' ')
        print(alturas[i], end=' - ')
        cont += 1

print(f'Existem {cont} alunos com idade a cima de 13 e altura abaixo da média.')