val = float(input('Digite o valor da casa que deseja comprar.  R$:'))
sal = float(input('O valor da parcela não pode exceder 30% de seu salário.\nDigite o seu salário.  R$:'))
anos = int(input('Digite em quantos anos deseja pagar a casa: '))
if val/(anos*12) > (sal*30)/100:
    print('Emprestimo negado!\nO valor da parcela é de R$:{:.2f} e excede o valor de 30% (R$:{:.2f}) em relação ao seu salário!' .format(val/(anos*12), (sal*30)/100))
elif val/(anos*12) < (sal*30)/100:
    print('Emprestimo concedido!\nO valor da parcela é de R$:{:.2f} e será pago em {} anos!' .format(val/(anos*12), anos))
else:
    print('Valor inválido.')