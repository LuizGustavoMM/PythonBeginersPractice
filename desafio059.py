print('Digite 2 valores e decida o que irá fazer com eles!!!')
escolha = 1
while escolha > 0:
    num1 = int(input('\n\n\n\n\nDigite o 1° número: '))
    num2 = int(input('Digite o 2° número: '))
    resposta = int(input('Digite o número da opção que você deseja.\n\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n\nResposta: '))
    if resposta == 1:
        print('\n\n\n\nA soma dos dois valores é de: {}' .format(num1+num2))
    elif resposta == 2:
        print('\n\n\n\nO produto da multiplicação dos dois valores é: {}' .format(num1*num2))
    elif resposta == 3:
        if num1 > num2:
            print('O maior valor digitado é: {}' .format(num1))
        else:
            print('O maior valor digitado é: {}' .format(num2))
    elif resposta == 4:
        escolha == 0
    else:
        escolha == 0
print('=-=' * 20)