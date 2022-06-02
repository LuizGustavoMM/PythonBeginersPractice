from datetime import date
idade = int(input('Digite sua idade atual e saiba sua cituação de alistamento no exército: '))
v = date.today().year
if idade < (18):
    print('Faltam {} anos para você se alistar e será em {}!' .format(18-idade, ((idade-18)*-1)+v))
elif idade == (18):
    print('Está na época de se alistar!')
else:
    print('Já se passaram {} anos da época de se alistar e foi no ano de {}!' .format(idade-18, (((idade-18))-v)*-1))
