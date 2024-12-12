dec = qnt = soma = 0
lista = []
res = 's'
while dec == 0:
    if res in 'SsSimsim':
        num = int(input('Digite um número: '))
        soma = num + soma
        lista.append(num)
        qnt += 1
        res = str(input('\nDeseja continuar?\n[S/N]\nResposta: '))
    else:
        dec += 1
print('\n\nQuantidade de números: {}\nMédia entre os número: {}\nMaior número: {}\nMenor número: {}' .format(qnt, soma/qnt, max(lista), min(lista)))