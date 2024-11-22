somaTotal = 0
precoMenor = 1000000000000000000
contProduto = 0

while True:
    nomeProduto = input('\nDigite o nome do produto: ')
    preco = int(input('\nDigite o preço do produto: R$'))
    somaTotal += preco

    if preco < precoMenor:
        precoMenor = preco
        produtoMenor = nomeProduto
    
    if preco > 1000:
        contProduto += 1

    continuar = input('\nDigite [S/N] para continuar.\nR:')

    if continuar in ('Ss'):
        continue
    
    if continuar in ('Nn'):
        break

print(f'\nTotal gasto na compra: R${somaTotal}')
print(f'\nProdutos custando mais de mil reais: {contProduto}')
print(f'\nProduto mais barato: {produtoMenor}')