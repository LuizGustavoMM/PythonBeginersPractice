print('Saiba sua média e descrubra se passou!')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
m = (n1 + n2 + n3)/3
if m >=7:
    print('Sua média é {:.1f}, parabéns você passou!' .format(m))
else:
    print('Sua média é {:.1f}, você não atingiu a média necessária para passar!' .format(m))
