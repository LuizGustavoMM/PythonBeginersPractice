peso = float(input('Calcule seu IMC de acordo com seu peso e altura.\n\nDigite sua peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
if imc <= 18.4:
    print('Seu IMC é de {:.1f} e está abaixo do peso ideal.' .format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.1f} e está entre o peso ideal.' .format(imc))
elif imc <=30:
    print('Seu IMC é de {:.1f} e está em sobrepeso.' .format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.1f} e é considerado obeso!' .format(imc))
elif imc > 40:
    print('Seu IMC é de {:.1f} e é considerado obesidade mórbida!!!' .format(imc))