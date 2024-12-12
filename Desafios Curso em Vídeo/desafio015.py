dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos Km foram rodados: '))
val = 60*dias
val1 = km * 0.15
val2 = val+val1
print('O valor total a ser pago pelo aluguel do carro é de R$:{:.2f}'.format(val2))