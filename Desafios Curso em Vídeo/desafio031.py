km = int(input('Digite quantos Km sua viagem terá e saiba quanto irá custar! '))
if km <= 200:
    print('Sua viagem custará: R${:.2f}'.format(km*0.50))
else:
    print('Sua viagem custará: R${:.2f}'.format(km*0.45))
