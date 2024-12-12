sal = float(input('Digite o valor do seu salário e saiba quanto irá aumentar. R$:'))
if sal <= 1250:
    print('O seu novo salário será R$:{}' .format(sal+(sal*15/100)))
else:
    print('O seu novo salária será R$:{}' .format(sal+(sal*15/100)))
