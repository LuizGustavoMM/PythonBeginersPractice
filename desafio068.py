import random
import time
cont = 0
while True:
    p1 = int(input('\nDigite \n[1] Papel\n[2] Pedra\n[3] Tesoura\n\nR: '))
    p2 = random.randint(1, 3)
    if p1 == p2:
        print('Empate! tente de novo')
        time.sleep(2)
    elif p1 == 1 and p2 == 2:
        cont += 1
        print(f'\nP1: Papel X P2: Pedra\nP1 Venceu!\nContador de vitórias: [{cont}]')
        time.sleep(2)
    elif p1 == 2 and p2 == 3:
        cont += 1
        print(f'P1: Pedra X P2: Tesoura\nP1 Venceu!\nContador de vitórias: [{cont}]')
        time.sleep(2)
    elif p1 == 3 and p2 == 1:
        cont += 1
        print(f'\nP1: Tesoura X P2: Papel\nP1 Venceu!\nContador de vitórias: [{cont}]')
        time.sleep(2)
    else:
        break
print('Você perdeu!')