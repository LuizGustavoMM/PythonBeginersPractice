num = int(input('Digite um número intiero e decida se quer ele em binário, octal ou hexadecimal: '))
dec = int(input('Digite "1" caso queira saber seu formato binário.\n\nDigite "2" caso queira saber seu formato octal.\n\nDigite "3" caso queira saber seu formato hexadecimal: '))
if dec == (1):
    print('O formato binário do número {} é: {}.' .format(num, bin(num)[2:]))
elif dec == 2:
    print('O formato octal do número {} é: {}' .format(num, oct(num)[2:]))
elif dec == 3:
    print('O formato hexadecimal do número {} é: {}' .format(num, hex(num)[2:]))
else:
    print('Opção inválida.')