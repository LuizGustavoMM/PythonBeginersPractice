'''print('Digite o peso de 5 pessoas e saiba o mais pesado.')
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o {}° peso:' .format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso
print('O maior peso da lista foi {}kg, e o menor peso foi {}kg.' .format(maior, menor))'''
print('Digite 5 pesos e saiba o maior.')
lista = []
for c in range(1, 6):
    peso = float(input('Digite o {}° peso: ' .format(c)))
    lista.append(peso)
print('O maior peso foi {}Kg.' .format(max(lista)))
