'''ano = int(input('Digite um ano e saiba se é bissexto ou não: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Ano bissexto!')
else:
    print('Não é bissexto!')'''
import calendar
ano = int(input('Digite um ano e saiba se é bissexto: '))
ano6 = calendar.isleap(ano)
if ano6 is True:
    print('O ano {}, é bissexto!'.format(ano))
else:
    print('O ano {}, não é bissexto!'.format(ano))