from random import randint
j = int(input('\033[1;34mBem vindo ao jogo de Pedra Papel ou tesoura, escolha uma das opções abaixo e jogue contra a máquina!\033[m\n\n1.Pedra\n2.Papel\n3.Tesoura\n\n\033[1;34mDigite o número de sua opção:\033[m '))
pc = randint(1, 3)
if pc == j:
    print('\033[1;33mAmbos jogaram {}.\n\nEmpate!\033[m'.format(j))
elif pc == 1 and j == 2:
    print('Você jogou papel e o computador jogou pedra.\n\n\033[1;32mParabéns você ganhou!\033[m')
elif pc == 2 and j == 1:
    print('Você jogou pedra e o computador jogou papel. \n\n\033[1;31mVocê perdeu!\033[m')
elif pc == 3 and j == 2:
    print('Você jogou papel e o computador jogou tesoura. \n\n\033[1;31mVocê perdeu!\033[m')
elif pc == 2 and j == 3:
    print('Você jogou tesoura e o computador jogou papel. \n\n\033[1;32mParabéns você ganhou!\033[m')
elif pc == 1 and j == 3:
    print('Você jogou tesoura e o computador jogou pedra. \n\n\033[1;31mVocê perdeu!\033[m')
elif pc == 3 and j == 1:
    print('Você jogou pedra e o computador jogou tesoura. \n\n\033[1;32mParabéns você ganhou!\033[m')
else:
    print('Jogada inválida!')