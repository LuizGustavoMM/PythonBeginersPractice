soma = 0

print('\nResponda as perguntas. Digite [1] para sim e [0] para não: \n')
resp = int(input('\nTelefonou para a vítima?\nR: '))
soma += resp
resp = int(input('\nEsteve no local do crime?\nR:'))
soma += resp
resp = int(input('\nMora perto da vítima?\nR:'))
soma += resp
resp = int(input('\nDevia para a vítima?\nR:'))
soma += resp
resp = int(input('\nJa trabalhou com a vítima?\nR:'))
soma += resp
if soma == 2:
    print('Classificado como suspeito!')
elif soma == 3 or soma == 4:
    print('Classificado como cúmplice!')
elif soma == 5:
    print('Classificado como assasino!')
else:
    print('Você é inocente!')