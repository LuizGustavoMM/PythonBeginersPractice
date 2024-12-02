import random
import time

cont = 0
while True:
    p1 = int(input('-----Par ou Ímpar-----\n\nEscolha [1] para Par ou [2] para Ímpar!\nR: '))
    p2 = random.randint(0, 10)
    n = int(input('Digite um número e saiba quem ganhou!\nR: '))
    s = n+p2
    if p1 == 1:
        if s % 2 == 0:
            cont += 1
            print(f'Você digitou {n} e o computador {p2}\n{n} + {p2} = {n+p2}\n')
            time.sleep(1)
        else:
            print(f'Você digitou {n} e o computador {p2}\n{n} + {p2} = {n+p2}\n')
            print(f'Você perdeu!\nNúmero de vitórias seguidas [{cont}]!')
            break

    if p1 == 2:
        if s % 2 == 1:
            cont += 1
            print(f'Você digitou {n} e o computador {p2}\n{n} + {p2} = {n+p2}\n\nVocê venceu! Contador de vitórias [{cont}]\n')
            time.sleep(1)
        else:
            print(f'Você digitou {n} e o computador {p2}\n{n} + {p2} = {n+p2}\n')
    print(f'Você perdeu!\nNúmero de vitórias seguidas [{cont}]!')
    break
        