vel = float(input('Digite a velocidade que o carro passou: '))
if vel <= 80:
    print('O carro está dentro dos limites!')
else:
    print('O carro está acima dos limites e a multa será de: R${:.2f},00'.format((vel-80)*7))
