c = s = 0
while True:
    n = int(input('Digite um número ou digite 999 para parar\nR: '))
    if n != 999:
        c += 1
        s = n + s
    else:
        break
print(f'\n\n\nA soma dos {c} números é de {s}.')