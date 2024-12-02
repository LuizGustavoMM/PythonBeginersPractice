extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20 e tenha ele por extenso: '))

while n not in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
    n = int(input('Digite um número entre 0 e 20 e tenha ele por extenso: '))
pos = n
print(f'O número por extenso que você digitou é {extenso[pos]}')