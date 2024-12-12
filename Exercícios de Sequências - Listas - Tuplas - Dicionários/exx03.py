lista = []

for i in range(4):
    nota = float(input(f'Digite o {i + 1}°: '))
    lista.append(nota)

soma = sum(lista)
print(soma/4)