lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print (len(lanche))
print(lanche[1:3])

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} em {cont}°')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} em {pos}°')

print('Comi pra caramba')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))