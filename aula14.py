n = 1
p = 0
i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        p += 1
    else:
        i += 1
print('Teve {} número pares e {} números impares.' .format(p, i))