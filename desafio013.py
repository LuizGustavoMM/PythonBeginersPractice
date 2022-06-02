print('Saiba quanto ficará seu salário com 15% de aumento!')
sal = float(input('Digite seu salário: '))
au = (15*sal)/100
salf = au+sal
print('Seu novo salário será de R${:.2f}.'.format(salf))