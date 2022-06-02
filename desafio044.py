preco = float(input('Digite o preço do produto e o método de pagamento e descubra se haverá descontos ou juros.\n\nPreço do produto.   R$:'))
metodo = int(input('Digite o número correspondente ao método de pagamento.\n\n1. À vista dinheiro/cheque (10% de desconto)\n2. À vista no cartão (5% de desconto)\n3. Em até 2x no cartão (preço normal)\n4. 3x ou mais no cartão (20% de juros)\nDigite o método de pagamento: '))
if metodo == 1:
    print('\n\nO o novo preço produto de R$:{:.2f} será de R$:{:.2f} com desconto de 10%.' .format(preco, preco - (preco * 10) / 100))
elif metodo == 2:
    print('\n\nO novo preço do produto de R$:{:.2f} será de R$:{:.2f} com desconto de 5%.' .format(preco, preco - (preco * 5) / 100))
elif metodo == 3:
    print('\n\nO preço do produto é deR$:{:.2f} e não haverá descontos nem acrescimos nessa forma de pagamento.' .format(preco))
elif metodo == 4:
    print('\n\nO preço do produto é de R$:{:.2f} e haverá acrescimo de (20%)\nnessa forma de pagamento e o novo preço será de R$:{:.2f}' .format(preco, preco + (preco * 20 / 100)))
else:
    print('\n\nOpção inválida.')