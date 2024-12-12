import random as rand
tupla = ()
lista = []

for numero in range(5):
    num = rand.randint(1, 100) 
    lista.append(num)
tupla = lista
print(f'Os valores sorteados foram: {tupla}')
print(f'Maior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')