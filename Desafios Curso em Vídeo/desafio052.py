n = int(input('Digite um número inteiro e saiba se é primo: '))
total = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} é divisivel {} vezes!' .format(n, total))
if total == 2:
    print('Este número é primo!')
else:
    print('Este número não é primo!')
