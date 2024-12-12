num1 = int(input('\033[1;100m\033[1;34mDigite dois números e saiba qual é maior.\033[m\n\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro número ({}) é maior que o segundo número ({}).' .format(num1, num2))
elif num2 > num1:
    print('O segundo número ({}) é maior que o primeiro número ({}).' .format(num2, num1))
else:
    print('Os número são iguais!')