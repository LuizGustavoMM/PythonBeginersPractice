vetor = [12, 45, 78, 34, 23, 56, 89, 67, 90, 11]
cont = 0
soma = 0

for i in vetor:
    print(f'Número {vetor[cont]} ao quadrado: ', vetor[cont] * vetor[cont])
    soma += vetor[cont] * vetor[cont]
    cont += 1 
print('A soma dos valores é: ', soma)