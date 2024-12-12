cont = somaTotal = contProduto = 0

while True:
    nomeProduto = str(input('\nDigite o nome do produto: '))
    preco = int(input('\nDigite o preço do produto: R$'))
    somaTotal += preco
    cont += 1

    if cont == 1 or preco < precoMenor:
        precoMenor = preco
        produtoMenor = nomeProduto
    
    if preco > 1000:
        contProduto += 1

    continuar = str(input('\nDigite [S/N] para continuar.\nR:')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(input('\nDigite [S/N] para continuar.\nR:')).strip().upper()[0]

    if continuar == 'S':  
        continue
    
    if continuar == 'N':
        break

print(f'\nTotal gasto na compra: R${somaTotal}')
print(f'\nProdutos custando mais de mil reais: {contProduto}')
print(f'\nProduto mais barato: {produtoMenor} custando: R$:{precoMenor}')