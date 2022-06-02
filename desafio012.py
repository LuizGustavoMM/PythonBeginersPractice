print('Calcule o preço de seu produto com o desconto de 5%')
pr = float(input('Digite o preço de seu produto: '))
por = (5*pr)/100
pf = pr-por
print('O preço final de seu produto é R${:.2f}.'.format(pf))
