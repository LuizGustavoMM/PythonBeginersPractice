idade = []
altura = []
cont = 0

for i in range(5):
    idd = int(input(f'Digite a {i+1}° idade: '))
    alt = float(input(f'Digite a {i+1}° altura: '))
    idade.append(idd)
    altura.append(alt)

for i in range(5):
    cont -= 1
    print(f'Idade: {idade[cont]} - Altura: {altura[cont]}')