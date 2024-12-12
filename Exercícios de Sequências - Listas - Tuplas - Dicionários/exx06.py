passou = []
cont = 0
ncont = 0

for i in range(10):
    nota = 0
    media = 0
    print(f'\nMédia do {i + 1}° aluno')
    for i in range(4):
        nota = float(input(f'Digite sua {i + 1}° nota: '))
        nota += nota
        media = nota/4
    if media >= 7:
        cont += 1
        passou.append(nota)
    else:
        ncont += 1

print(f'Número de pessoas que passaram {cont}\nMédias de quem passou: {cont}')
print('Número de pessoas que não passaram: ', ncont)
