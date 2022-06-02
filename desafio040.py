n1 = float(input('Digite suas notas e saiba se foi aprovado ou não.\n\nPrimeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
mf = (n1+n2+n3)/3
if mf < 4.9:
    print('Você foi reprovado com a média de {:.1f}' .format(mf))
elif mf >= 5.0 and mf <= 6.9:
    print('Você está de recuperação com a média de {:.1f}' .format(mf))
elif mf >= 7.0 and mf <=10:
    print('Parabéns você foi aprovado com a média de {:.1f}!' .format(mf))