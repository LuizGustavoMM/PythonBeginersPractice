from datetime import date
ano = int(input('Digite sua idade e saiba qual sua classificção etária na confederação nacional de natação!\n\n Digite sua idade: '))
idade = date.today().year-ano
if idade <= 9:
    print('Com a idade de {} anos, você é considerado mirim!' .format(idade))
elif idade <= 14:
    print('Com a idade de {} anos, você é considerado infantil!' .format(idade))
elif idade <= 19:
    print('Com a idade de {} anos, você é considerado junior!' .format(idade))
elif idade <= 25:
    print('Com a idade de 20 anos você é considerado sênior!' .format(idade))
elif idade > 25:
    print('Com a idade de {} anos, você é considerado master!' .format(idade))
